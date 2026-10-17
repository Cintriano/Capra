# CAPRA — Kit de logos filhas (v1.6)

Tudo o que é preciso para criar a marca de qualquer produto da CAPRA pelo método do disco orbital. A regra completa está em `docs/08-logos-filhas.md`.

## Caminho mais simples: gerador web

Abra **https://claude.ai/artifact/DUtbn26g1yLTa4xe4g5734**, digite o nome do produto, escolha a área e o neutro, clique em **Registrar produto** e depois em **Baixar pacote (.zip)**. O registro de produtos fica salvo na ferramenta e decide as colisões de letras.

`ferramenta/gerador-logos-filhas.html` é uma cópia da mesma página. Aberta localmente, ela mostra a prévia e calcula a marca, mas não tem o registro compartilhado nem os downloads; use a versão publicada.

## Pelo script (para gerar em lote ou integrar a um pipeline)

Requer Python 3.8+. Nenhuma dependência; para exportar PNG, instale `cairosvg` (`pip install cairosvg`), senão o script gera só SVG.

```bash
cd gerador

# que marca este nome receberia?
python capra_filhas.py letras "Nome do Produto"

# registrar um produto novo e gerar os arquivos
python capra_filhas.py novo "Nome do Produto" --area dados --neutro branco

# gerar todos os produtos do registro (ou um só com --produto)
python capra_filhas.py gerar
python capra_filhas.py gerar --produto Ravix
```

Os arquivos saem em `gerador/logos/<produto>/`:

| Arquivo | Uso |
|---|---|
| `<produto>-icone-app.svg` + PNG 1024/512/192/180 | Ícone de app e PWA |
| `<produto>-icone-reduzido.svg` | Abaixo de 32 px |
| `<produto>-favicon.svg` + PNG 48/32/16 | Favicon |
| `<produto>-marca.svg` | Marca sem fundo, só sobre o neutro do produto |
| `<produto>-entrada.svg` | Entrada animada (0,8 s), com as mesmas regras de fundo da marca; regras na Parte 11 do manual |

Áreas: `plataforma` (Ciano), `dados` (Lilás), `automacao` (Mint), `financas` (Peach), `infraestrutura` (Gold). Neutros: `preto`, `branco`.

## Registro

`gerador/registro.csv` tem as colunas `produto, marca, area, neutro, data, observacoes`. Produtos sem área ou neutro definidos são pulados na geração. A ordem das linhas é a ordem de registro: quem vem primeiro fica com a letra única. Nunca altere a coluna `marca` de um produto já lançado. Mantenha o CSV igual ao registro do gerador web.

## Conteúdo

```text
alfabeto/
  capra-alfabeto.json        letras A–Z, algarismos 0–9 e sinais (contornos e perfis de espaçamento)
  capra-alfabeto-prova.svg   prova com letras, algarismos e sinais
  svg/letra-A.svg …          um caractere por arquivo (letra-, algarismo-, sinal-)
gerador/
  capra_filhas.py            script
  capra-alfabeto.json        cópia usada pelo script (igual à de alfabeto/)
  registro.csv               registro de produtos
ferramenta/
  gerador-logos-filhas.html  cópia do gerador web
logos/ravix/                 exemplo completo gerado pelo script (inclui a entrada animada)
docs/08-logos-filhas.md      regras, com figuras embutidas
```
