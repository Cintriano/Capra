#!/usr/bin/env python3
"""
CAPRA — gerador de logos filhas (v1.3)

Gera a marca de um produto pelo método do "disco orbital":
disco na cor do acento + letra(s) recortada(s) + dois braços de órbita.

Uso:
  python capra_filhas.py novo "Nome do Produto" --area financas --neutro preto
  python capra_filhas.py gerar                      # gera todos os produtos do registro
  python capra_filhas.py gerar --produto Ravix      # gera só um
  python capra_filhas.py letras "Nome"              # mostra a(s) letra(s) que o nome receberia

Arquivos esperados (mesma pasta deste script, ou indique com --alfabeto / --registro):
  capra-alfabeto.json   letras A–Z desenhadas para a CAPRA
  registro.csv          lista de produtos (produto, marca, area, neutro, data, observacoes)

Só usa a biblioteca padrão do Python 3.8+. Para PNG, instale cairosvg (opcional):
  pip install cairosvg
"""
import argparse, csv, datetime, json, math, os, sys, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- cores
NEUTROS = {"preto": "#121416", "branco": "#FFFFFF"}
# área -> (acento pastel, usado com neutro preto; acento profundo, usado com neutro branco)
AREAS = {
    "plataforma":     ("#8FB8C5", "#3B6A79"),   # Ciano: plataforma e produtos fora das quatro áreas
    "dados":          ("#B3A6C9", "#665789"),   # Lilás
    "automacao":      ("#9DBBAA", "#45705A"),   # Mint
    "financas":       ("#D7AFA3", "#93503E"),   # Peach
    "infraestrutura": ("#D6C58F", "#776220"),   # Gold
}

def cor_do_disco(area, neutro):
    pastel, profundo = AREAS[area]
    return pastel if neutro == "preto" else profundo

# ---------------------------------------------------------------- geometria da marca
R = 100.0                        # raio do disco
BRACO = dict(gap=10.0, w0=28.0, w1=9.0, grow=36.0, a0=170.0, sweep=168.0)
LETRA_UMA = 0.42                 # altura da letra única = 0,42 × diâmetro
DIAG_MAX = 0.74                  # meia-diagonal máxima do bloco de letras, em raios
DIAG_MAX_REDUZIDO = 0.84         # no ícone reduzido (sem braços) as duas letras podem crescer
ESPACO_PAR = 12.0                # menor distância horizontal entre duas letras (unidades da letra)
OCUPA_ICONE = 0.68               # largura da marca completa no ícone de app
OCUPA_REDUZIDO = 0.74            # largura do disco no ícone reduzido

def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")

def _d(contornos):
    return "".join("M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in c) + " Z" for c in contornos)

def _circulo(r, n=160):
    return [(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n)) for i in range(n)]

def _braco(a0):
    p = BRACO
    rho0 = R + p["gap"] + p["w0"] / 2
    b = math.log((rho0 + p["grow"]) / rho0) / math.radians(p["sweep"])
    esq, dir_ = [], []
    n = 240
    for i in range(n + 1):
        t = i / n
        ph = math.radians(p["sweep"]) * t
        a = math.radians(a0) + ph
        rho = rho0 * math.exp(b * ph)
        w = p["w0"] + (p["w1"] - p["w0"]) * t ** 0.9
        x, y = rho * math.cos(a), rho * math.sin(a)
        dx = b * math.cos(a) - math.sin(a); dy = b * math.sin(a) + math.cos(a); l = math.hypot(dx, dy)
        nx, ny = dy / l, -dx / l
        esq.append((x + nx * w / 2, y + ny * w / 2)); dir_.append((x - nx * w / 2, y - ny * w / 2))
    return esq + dir_[::-1]

BRACOS = [_braco(BRACO["a0"]), _braco(BRACO["a0"] + 180)]

def _bbox(pts):
    xs = [x for x, y in pts]; ys = [y for x, y in pts]
    return min(xs), min(ys), max(xs), max(ys)

# ---------------------------------------------------------------- letras
class Alfabeto:
    def __init__(self, caminho):
        with open(caminho, encoding="utf-8") as fh:
            self.dados = json.load(fh)["letras"]

    def bloco(self, letras):
        """posiciona 1 ou 2 letras lado a lado; devolve contornos em unidades da letra (altura 100)"""
        contornos, x = [], 0.0
        anterior = None
        for ch in letras:
            g = self.dados[ch]
            if anterior is not None:
                # menor distância entre o perfil direito da anterior e o esquerdo desta
                pd, pe = anterior["perfilDir"], g["perfilEsq"]
                avanco = max((pd[i] + ax) - pe[i] for i in range(101) if pd[i] is not None and pe[i] is not None)
                x = avanco + ESPACO_PAR
            for c in g["contornos"]:
                contornos.append([(px + x, py) for px, py in c])
            anterior, ax = g, x
        return contornos

    def no_disco(self, letras, diag_max=DIAG_MAX):
        """escala e centraliza as letras dentro do disco"""
        cs = self.bloco(letras)
        x0, y0, x1, y1 = _bbox([p for c in cs for p in c])
        w, h = x1 - x0, y1 - y0
        k = (LETRA_UMA * 2 * R) / h                       # altura padrão
        meia_diag = math.hypot(w * k / 2, h * k / 2)
        if meia_diag > diag_max * R:                       # bloco largo demais: reduz
            k *= diag_max * R / meia_diag
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        return [[((px - cx) * k, (py - cy) * k) for px, py in c] for c in cs]

# ---------------------------------------------------------------- regra das letras
VOGAIS = set("AEIOU")

def normalizar(nome):
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().upper()
    return "".join(ch for ch in s if "A" <= ch <= "Z")

def letras_para(nome, ocupadas):
    """primeira letra; em colisão, acrescenta a próxima consoante do nome (e a seguinte, se preciso)"""
    s = normalizar(nome)
    if not s:
        raise ValueError(f'"{nome}" não tem letras de A a Z para formar a marca.')
    if s[0] not in ocupadas:
        return s[0]
    for ch in s[1:]:
        if ch not in VOGAIS and s[0] + ch not in ocupadas:
            return s[0] + ch
    for ch in s[1:]:                                       # sem consoante livre: tenta as vogais
        if s[0] + ch not in ocupadas:
            return s[0] + ch
    raise ValueError(f'Não há combinação livre para "{nome}". Defina a marca à mão no registro.')

# ---------------------------------------------------------------- SVG
def _grupo(alfa, letras, cor, tx, ty, k, bracos=True):
    disco = _circulo(R)
    g = f'<g transform="translate({_f(tx)} {_f(ty)}) scale({_f(k)})" fill="{cor}">'
    letras_cs = alfa.no_disco(letras, DIAG_MAX if bracos else DIAG_MAX_REDUZIDO)
    g += f'<path d="{_d([disco] + letras_cs)}" fill-rule="evenodd"/>'
    if bracos:
        for b in BRACOS:
            g += f'<path d="{_d([b])}"/>'
    return g + "</g>"

def _limites(bracos=True):
    pts = _circulo(R)
    if bracos:
        for b in BRACOS:
            pts += b
    return _bbox(pts)

def svg_marca(alfa, letras, cor, titulo):
    x0, y0, x1, y1 = _limites(True)
    w, h = x1 - x0, y1 - y0
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {_f(w)} {_f(h)}" role="img" aria-label="{titulo}">'
            f"<title>{titulo}</title>{_grupo(alfa, letras, cor, -x0, -y0, 1)}</svg>\n")

def svg_icone(alfa, letras, fundo, cor, titulo, tamanho=1024, bracos=True, raio=0):
    x0, y0, x1, y1 = _limites(bracos)
    ocupa = OCUPA_ICONE if bracos else OCUPA_REDUZIDO
    k = tamanho * ocupa / max(x1 - x0, y1 - y0)
    tx = tamanho / 2 - (x0 + x1) / 2 * k; ty = tamanho / 2 - (y0 + y1) / 2 * k
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {tamanho} {tamanho}" role="img" aria-label="{titulo}">'
            f'<title>{titulo}</title><rect width="{tamanho}" height="{tamanho}" rx="{_f(raio)}" fill="{fundo}"/>'
            f"{_grupo(alfa, letras, cor, tx, ty, k, bracos)}</svg>\n")

# ---------------------------------------------------------------- registro
CAMPOS = ["produto", "marca", "area", "neutro", "data", "observacoes"]

def ler_registro(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, encoding="utf-8", newline="") as fh:
        return [{k: (v or "").strip() for k, v in linha.items()} for linha in csv.DictReader(fh)]

def gravar_registro(caminho, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, lineterminator="\n")
        w.writeheader()
        for l in linhas:
            w.writerow({k: l.get(k, "") for k in CAMPOS})

# ---------------------------------------------------------------- saída
def slug(nome):
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return "".join(ch if ch.isalnum() else "-" for ch in s).strip("-")

def gerar_produto(alfa, linha, saida, png=True):
    produto, letras, area, neutro = linha["produto"], linha["marca"], linha["area"], linha["neutro"]
    if area not in AREAS or neutro not in NEUTROS:
        print(f"  ! {produto}: área ou neutro não definidos no registro; pulei.")
        return
    cor = cor_do_disco(area, neutro); fundo = NEUTROS[neutro]
    pasta = os.path.join(saida, slug(produto)); os.makedirs(pasta, exist_ok=True)
    base = slug(produto)
    arquivos = {
        f"{base}-icone-app.svg": svg_icone(alfa, letras, fundo, cor, f"{produto} — ícone de app"),
        f"{base}-icone-reduzido.svg": svg_icone(alfa, letras, fundo, cor, f"{produto} — ícone reduzido", bracos=False),
        f"{base}-favicon.svg": svg_icone(alfa, letras, fundo, cor, f"{produto} — favicon", tamanho=64, bracos=False, raio=12),
        f"{base}-marca.svg": svg_marca(alfa, letras, cor, f"{produto} — marca"),
    }
    for nome, conteudo in arquivos.items():
        with open(os.path.join(pasta, nome), "w", encoding="utf-8") as fh:
            fh.write(conteudo)
    if png:
        try:
            import cairosvg
            for px in (1024, 512, 192, 180):
                cairosvg.svg2png(bytestring=arquivos[f"{base}-icone-app.svg"].encode(), write_to=os.path.join(pasta, f"{base}-icone-app-{px}.png"), output_width=px, output_height=px)
            for px in (48, 32, 16):
                cairosvg.svg2png(bytestring=arquivos[f"{base}-icone-reduzido.svg"].encode(), write_to=os.path.join(pasta, f"{base}-favicon-{px}.png"), output_width=px, output_height=px)
        except ImportError:
            print("  (cairosvg não instalado: gerei só os SVGs)")
    print(f"  ✓ {produto}: {letras} · {area} · {neutro} → {pasta}")

# ---------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser(description="CAPRA — gerador de logos filhas")
    ap.add_argument("--alfabeto", default=os.path.join(AQUI, "capra-alfabeto.json"))
    ap.add_argument("--registro", default=os.path.join(AQUI, "registro.csv"))
    ap.add_argument("--saida", default=os.path.join(AQUI, "logos"))
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("novo", help="registra um produto novo e gera a marca")
    n.add_argument("nome"); n.add_argument("--area", required=True, choices=sorted(AREAS))
    n.add_argument("--neutro", required=True, choices=sorted(NEUTROS))
    n.add_argument("--obs", default="")
    g = sub.add_parser("gerar", help="gera os arquivos dos produtos do registro")
    g.add_argument("--produto"); g.add_argument("--sem-png", action="store_true")
    l = sub.add_parser("letras", help="mostra a(s) letra(s) que um nome receberia")
    l.add_argument("nome")
    a = ap.parse_args()

    registro = ler_registro(a.registro)
    ocupadas = {r["marca"] for r in registro if r.get("marca")}

    if a.cmd == "letras":
        existente = next((r for r in registro if r["produto"].lower() == a.nome.lower()), None)
        if existente:
            print(f'{a.nome} já está no registro com a marca {existente["marca"]} (marcas lançadas não mudam).')
        else:
            print(letras_para(a.nome, ocupadas))
        return

    alfa = Alfabeto(a.alfabeto)
    if a.cmd == "novo":
        if any(r["produto"].lower() == a.nome.lower() for r in registro):
            sys.exit(f'"{a.nome}" já está no registro.')
        letras = letras_para(a.nome, ocupadas)
        linha = {"produto": a.nome, "marca": letras, "area": a.area, "neutro": a.neutro,
                 "data": datetime.date.today().isoformat(), "observacoes": a.obs}
        registro.append(linha); gravar_registro(a.registro, registro)
        print(f'Registrado: {a.nome} → {letras}')
        gerar_produto(alfa, linha, a.saida)
    else:
        alvo = [r for r in registro if not a.produto or r["produto"].lower() == a.produto.lower()]
        if not alvo:
            sys.exit("Nenhum produto encontrado no registro.")
        for r in alvo:
            gerar_produto(alfa, r, a.saida, png=not a.sem_png)

if __name__ == "__main__":
    main()
