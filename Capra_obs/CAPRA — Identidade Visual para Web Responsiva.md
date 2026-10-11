# CAPRA — Identidade Visual para Web Responsiva

Oct 11, 2026 · @Danilo Fernandes

## Introdução

Este documento aplica o manual de marca CAPRA v1.3 à web, com um único layout que se adapta do celular ao desktop. Ele não muda nenhuma regra do manual: define faixas de largura, como cada elemento muda entre elas e o que a implementação precisa garantir.

| Tipo de produto web | Exemplos | Foco |
| --- | --- | --- |
| Site institucional | Site da CAPRA, páginas de produto | Leitura, apresentação, contato |
| Aplicação web | Ravix, Clam e Melope no navegador | Tarefas, formulários, navegação entre áreas |
| Painel de dados | DW\_APOLO | Tabelas, gráficos, filtros |
| PWA | Qualquer aplicação instalável pelo navegador | Ícone, abertura e uso sem barra do navegador |

**Unidades.** Medidas do manual em px valem como px de CSS. Texto usa `rem` (1 rem = 16 px no padrão do navegador), para respeitar o tamanho de fonte que a pessoa escolheu.

**Relação com o documento mobile.** As faixas de largura e as alturas de toque são as mesmas do documento de apps mobile, para que web e app tenham o mesmo comportamento. Itens marcados como **proposta** não existem no manual v1.3 e precisam de aprovação para a v1.4.

## Princípios de responsividade

Um só HTML se reorganiza em todas as larguras: nada de site móvel separado. O que muda entre celular e desktop é a disposição; a marca, os tokens e o conteúdo essencial são os mesmos.

- **Mobile first no código.** O CSS base desenha a tela mais estreita; regras com `min-width` acrescentam colunas e detalhes.
- **O conteúdo define a quebra.** A página muda pela largura da janela; cada componente muda pela largura do próprio espaço (container queries).
- **Entrada não é tamanho.** Hover e precisão dependem do ponteiro (`hover`, `pointer`), não da largura: há notebooks com toque e tablets com teclado.
- **Dark first continua valendo.** O site abre no tema do sistema; desenho e revisão começam pelo dark.
- **A marca troca de versão, não encolhe.** Abaixo do tamanho mínimo, a assinatura horizontal dá lugar ao símbolo.
- **Nada essencial some.** Em telas pequenas, o conteúdo muda de lugar ou vai para um menu; só decoração (pontos extras, texto de apoio de banner) pode sair.

## Breakpoints, grid e containers

Cinco faixas de largura, com as mesmas quebras de 600 e 840 dos apps mobile. Os nomes de token são proposta; os valores de margem e espaço vêm da escala do manual.

| Token (proposta) | Largura da janela | Exemplos | Colunas | Margem lateral | Espaço entre colunas | Largura máxima do conteúdo |
| --- | --- | --- | --- | --- | --- | --- |
| `bp-xs` (base) | 320 a 599 px | Celulares | 4 | 16 | 16 | Toda a largura |
| `bp-sm` | 600 a 839 px | Tablet em retrato, celular em paisagem | 8 | 24 | 24 | Toda a largura |
| `bp-md` | 840 a 1199 px | Tablet em paisagem, notebook pequeno | 12 | 32 | 24 | Toda a largura |
| `bp-lg` | 1200 a 1599 px | Notebook, desktop | 12 | 48 | 24 | 1200 px no site |
| `bp-xl` | 1600 px ou mais | Monitores grandes | 12 | 48 | 32 | 1440 px no site |

### Containers

- **Site:** conteúdo centralizado na largura máxima da faixa. Banners e faixas de cor vão de borda a borda; o conteúdo dentro deles respeita o container.
- **Aplicação e painel:** usam toda a largura da janela, com barra lateral e área de conteúdo fluida. Formulários ficam com no máximo 640 px.
- **Texto corrido:** no máximo 80 caracteres por linha (`max-inline-size: 80ch`), como diz o manual.
- **Largura mínima:** tudo funciona em 320 px sem rolagem horizontal da página.

### Espaço vertical

| Entre | Celular | Desktop |
| --- | --- | --- |
| Itens de um grupo | 8 (`space-sm`) | 8 (`space-sm`) |
| Grupos de conteúdo | 24 (`space-lg`) | 24 (`space-lg`) |
| Seções de página | 32 (`space-xl`) | 48 (`space-xxl`) |
| Respiro interno de banners | 24 (`space-lg`) | 48 (`space-xxl`) |

## Layout por breakpoint

Os destinos e o conteúdo são os mesmos nas três faixas; muda onde a navegação fica e quantas colunas cabem lado a lado.

&#91;embedded content: Layout do site e da aplicação web nas três faixas de largura\]

Em destaque: ação principal, item ativo e a espiral do banner. No site, a espiral sai pela borda direita em todas as faixas; na aplicação, a navegação vai da barra inferior no celular para a barra lateral fixa no desktop.

## Logo na web

A assinatura horizontal é a marca do cabeçalho em todas as larguras: ela cresce com a janela, mas nunca fica abaixo de 120 px. Produtos usam a própria assinatura no cabeçalho e o endosso CAPRA no rodapé.

### Cabeçalho e rodapé

| Faixa | Altura do cabeçalho (proposta) | Site CAPRA | Site de produto |
| --- | --- | --- | --- |
| `bp-xs` | 56 px | Horizontal com X = 12 px (cerca de 121 px de largura) | Assinatura do app com nome em 16 px |
| `bp-sm` e `bp-md` | 64 px | Horizontal com X = 14 px (cerca de 141 px) | Nome em 18 px |
| `bp-lg` e `bp-xl` | 72 px | Horizontal com X = 16 px (cerca de 162 px) | Nome em 20 px |

X é a altura das letras do logotipo; a largura total da horizontal é 10,1X. A área de proteção de 0,5X vale em todas as faixas.

- **Rodapé:** site CAPRA com a assinatura horizontal; site de produto com a assinatura com endosso (marca, nome, fio, "por" e logotipo CAPRA).
- **Link:** o logo leva à página inicial e tem texto alternativo com o nome, como "CAPRA, página inicial".
- **Arquivo, nunca texto:** o nome CAPRA no cabeçalho é sempre o SVG do logotipo.
- **Troca de tema:** duas imagens, `capra-horizontal.svg` e `capra-horizontal-fundo-claro.svg`, alternadas pelo CSS conforme o tema ativo. Não recolorir o SVG por código: o gradiente do símbolo é só dos arquivos.

### Favicon, PWA e compartilhamento

| Arquivo | Medida | Uso |
| --- | --- | --- |
| `capra-favicon.svg` | Vetor | Favicon principal |
| Favicon PNG | 16, 32 e 48 px | Navegadores sem suporte a SVG |
| `apple-touch-icon` | 180 px | "Adicionar à tela de início" no iOS |
| Ícones do manifesto PWA | 192 e 512 px | Instalação; o de 512 também marcado como mascarável |
| Imagem de compartilhamento (Open Graph) | 1200 × 630 px | Prévia de links em redes e mensageiros |
| `theme-color` | #121416 no dark, #F3F5F6 no claro | Cor da barra do navegador no celular |
| `background_color` do manifesto | Neutro do produto ou #121416 | Tela de abertura do PWA |

- **Ícone mascarável:** o ícone de app serve como está se a marca (64% ou 68% da largura) couber na zona segura circular de 80%. Confira o recorte do símbolo CAPRA numa ferramenta de prévia de ícones mascaráveis.
- **Produtos:** usam os arquivos do gerador de logos filhas. Abaixo de 32 px, o favicon é a versão reduzida (disco e letra).
- **Imagem de compartilhamento:** composição de banner do manual, com título e marca no centro, para continuar legível quando a plataforma corta a imagem em quadrado.

## Cores e temas

As cores são variáveis CSS geradas de `capra-tokens.json`, com os temas Dark e Light do manual; cada produto troca só o acento. Responsividade não muda cor: celular e desktop usam exatamente os mesmos tokens.

```css
:root {
  color-scheme: dark light;
  --background: #121416;
  --surface: #181b1e;
  --text-primary: #e8ecee;
  --accent: #8fb8c5;
  /* demais tokens Dark */
}
:root[data-theme="light"] {
  --background: #f3f5f6;
  --text-primary: #121416;
  --accent: #3b6a79;
  /* demais tokens Light */
}
[data-product="ravix"] { --accent: var(--accent-finance); }
```

- **Tema.** O site segue `prefers-color-scheme` e oferece a escolha Sistema, Escuro ou Claro. A escolha é aplicada por um script curto no `<head>`, antes da primeira pintura, para não piscar o tema errado.
- **`color-scheme`** declarado, para barras de rolagem, campos nativos e preenchimento automático seguirem o tema.
- **`theme-color`** com uma meta por tema, para a barra do navegador no celular acompanhar o fundo.
- **Seleção de texto** com fundo no acento e texto `onAccent`.
- **Barras de rolagem** em painéis: alça `borderStrong` sobre trilho `surface`.
- **Cores forçadas** (alto contraste do Windows): bordas e ícones usam `currentColor` ou bordas transparentes, que o navegador torna visíveis. Nada de informação só em sombra ou fundo.
- **Impressão:** `@media print` aplica o tema claro.
- **Acentos:** um por produto. Páginas da CAPRA que apresentam produtos usam no máximo dois acentos ao mesmo tempo.

## Tipografia responsiva

No desktop vale a escala digital do manual; no celular, a escala mobile proposta no documento de apps, com corpo de 16 px. A troca acontece em 840 px; só o Display é fluido entre as faixas.

| Nível | Abaixo de 840 px | 840 px ou mais | Peso |
| --- | --- | --- | --- |
| Display | Fluido, de 34 / 40 em 360 px a 40 / 48 em 1200 px: `clamp(2.125rem, 1.964rem + 0.714vw, 2.5rem)` | Mesmo valor fluido; 40 / 48 a partir de 1200 px | Bold 700 |
| H1 | 28 / 34 | 28 / 36 | Bold 700 |
| H2 | 20 / 26 | 20 / 28 | Bold 700 |
| Body (aplicação e painel) | 16 / 24 | 14 / 22 | Regular 400 |
| Body (site e textos longos) | 16 / 24 | 16 / 26 (proposta) | Regular 400 |
| Rótulo de botão e campo | 16 / 20 | 14 / 20 | Medium 500 |
| Caption | 13 / 18 | 12 / 16 | Regular 400 |
| Code | 13 / 20 | 12 / 18 | JetBrains Mono 400 |

Valores em px, tamanho / entrelinha; no CSS, em `rem`.

### Regras

- **`rem` sempre.** Nunca fixe o `font-size` do `html` em px: isso ignora o tamanho de fonte escolhido no navegador.
- **Campos com 16 px no celular.** O Safari do iOS dá zoom automático em campos com texto menor que 16 px.
- **Fluido só no grande.** `clamp()` só em Display e títulos de banner; texto de leitura muda em degraus.
- **Medida:** até 80 caracteres por linha; `text-wrap: balance` em títulos e `pretty` em parágrafos.
- **Hifenização** (`hyphens: auto`, com `lang="pt-BR"`) em colunas estreitas no celular.
- **Números tabulares** em tabelas, valores e painéis (`font-variant-numeric: tabular-nums`).

### Carregamento

- Inter variável auto-hospedada em WOFF2, subconjunto latino com os acentos do português, `font-display: swap`.
- `preload` só do arquivo de texto principal; fonte de reserva com `size-adjust` próximo da Inter, para o texto não pular quando a fonte chega.
- JetBrains Mono carregada só em páginas com código ou dados técnicos.

## Navegação e estrutura

A navegação muda de forma em 600 e 840 px, as mesmas quebras dos apps, mas os destinos e a ordem são os mesmos em todas as larguras. Quem aprende o site no celular reconhece o desktop.

| Elemento | Celular (até 599 px) | Tablet (600 a 839 px) | Desktop (840 px ou mais) |
| --- | --- | --- | --- |
| Cabeçalho do site | Logo e botão Menu | Logo, até 3 links e botão Menu | Logo, links principais e ação principal à direita |
| Menu do site | Painel em tela cheia, links em H2 com 56 de altura, ação principal no fim | Painel lateral de 360 px | Links visíveis; submenus em painel sob o cabeçalho |
| Navegação da aplicação | Barra inferior com 3 a 5 destinos, como no app | Trilho lateral de 72 px com ícone e rótulo curto | Barra lateral fixa de 240 a 280 px, recolhível para trilho |
| Ação principal da tela | Botão no rodapé, largura total | Botão no topo da página | Botão no topo da página |
| Busca | Ícone que abre o campo em tela cheia | Campo no cabeçalho | Campo no cabeçalho, com atalho de teclado |
| Trilha de navegação | Só o nível anterior: "← Voltar para Produtos" | Completa | Completa |
| Rodapé | Uma coluna | Duas colunas | Quatro colunas e assinatura |

- **Cabeçalho fixo** no topo, com fundo `background` opaco e divisória `border` depois de rolar. Sem transparência nem desfoque.
- **"Pular para o conteúdo"** é o primeiro link da página, visível ao receber foco.
- **Painéis de menu** fecham com Esc, com o botão Fechar e com toque fora; o foco volta ao botão que abriu.
- **Item ativo** com texto no acento e indicador `surfaceElevated`, como nos apps.

## Componentes responsivos

Os componentes do manual mantêm cores, raios e bordas em qualquer largura; mudam o tamanho do alvo, a disposição e a forma de abrir. Tamanho de alvo depende do ponteiro, disposição depende do espaço.

| Componente | Celular e toque | Desktop e mouse |
| --- | --- | --- |
| Botão | Altura 48 com `pointer: coarse`. Primário com largura total em formulários | Altura 40, como no manual, largura do rótulo |
| Campo | Altura 48, texto de 16 px, uma coluna | Altura 40. Duas colunas só para campos curtos e ligados, como cidade e estado |
| Grade de cartões | Uma coluna | `repeat(auto-fill, minmax(280px, 1fr))`: de 2 a 4 colunas |
| Cartão | Conteúdo empilhado | Com 480 px ou mais de largura própria (container query), imagem ou gráfico ao lado do texto |
| Tabela | Até 4 colunas: rolagem horizontal dentro da tabela, primeira coluna fixa. Mais que isso: uma linha vira um cartão | Tabela completa, cabeçalho fixo ao rolar |
| Diálogo | Tela cheia ou folha inferior, ações fixas no rodapé | Centralizado, 480 a 640 px, `radius-lg` |
| Menu suspenso | Folha inferior | Painel ancorado ao botão |
| Dica (tooltip) | Não existe sem hover: a informação vira texto de ajuda visível | Só complemento; nunca informação essencial |
| Abas | Linha rolável na horizontal | Lado a lado |
| Filtros de painel | Botão "Filtros (3)" que abre uma folha | Coluna lateral de filtros |
| Paginação | Anterior e Próxima, ou "Carregar mais" | Números de página |
| Gráfico | Menos marcas no eixo, legenda acima, valor ao tocar | Valor ao passar o mouse, legenda ao lado |

- **Texto nunca encolhe abaixo de `caption`** para caber: o componente reorganiza ou rola.
- **Rolagem horizontal** só dentro de um componente (tabela, abas, carrossel), nunca na página.
- **Gráficos** mantêm uma cor principal e as cores de estado; no celular, mostre menos séries em vez de cores mais finas.

## Interação

O comportamento acompanha o tipo de entrada que o navegador informa, e não a largura da tela. Uma mesma página precisa funcionar com mouse, toque e teclado ao mesmo tempo.

| Entrada | Como detectar | Comportamento |
| --- | --- | --- |
| Mouse ou trackpad | `@media (hover: hover) and (pointer: fine)` | Hover muda a luminosidade em cerca de 8%, como no manual. Alvos de 40 px |
| Toque | `@media (pointer: coarse)` ou `(any-pointer: coarse)` | Sem hover; estado pressionado com `:active`. Alvos de 44 a 48 px com 8 px entre eles |
| Teclado | `:focus-visible` | `focus-ring`: respiro na cor do fundo e anel de 2 px no acento. Ordem de tabulação igual à ordem visual |

- **Hover nunca é o único caminho.** Menus e detalhes abrem com clique, toque e Enter.
- **Estilos de hover só dentro de `@media (hover: hover)`**, para não ficarem presos depois de um toque.
- **Gestos são atalho.** Deslizar para excluir ou fechar sempre tem um botão equivalente.
- **Zoom liberado.** Nunca use `user-scalable=no` nem `maximum-scale=1` na meta viewport.
- **Atalhos de teclado** nas aplicações: `/` foca a busca, Esc fecha painéis e diálogos. Atalhos aparecem nos menus ao lado da ação.

## Imagens, banners e linguagem gráfica

O banner segue o manual (fragmento de espiral, poucos pontos, espaço negativo, assinatura pequena) e se recompõe por faixa. No celular o texto vem primeiro; no desktop, texto e espiral dividem a largura.

| Faixa | Composição do banner |
| --- | --- |
| Celular | Título em Display, subtítulo e botão com largura total. Espiral recortada abaixo do texto, saindo pela borda direita. 2 ou 3 pontos |
| Tablet | Texto em cerca de 60% da largura, à esquerda. Espiral à direita, saindo do enquadramento. 3 ou 4 pontos |
| Desktop | Texto nas colunas 1 a 6, espiral nas colunas 7 a 12 saindo pela borda. Até 5 pontos e assinatura pequena |

- **Espiral em SVG**, nunca em imagem rasterizada, e nunca o logo ampliado: o manual pede parte da espiral, não o símbolo repetido grande.
- **Texto nunca sobre a espiral.** A espiral fica no espaço negativo.
- **Ilustrações** em SVG com cores por variável CSS, para funcionar nos dois temas. O logo é exceção: usa os arquivos por tema.
- **Direção de arte** com `<picture>` quando o recorte muda entre faixas; `srcset` e `sizes` em fotos.
- **Proporção reservada** com `aspect-ratio` em toda imagem e banner, para o layout não pular.
- **Fotos** escuras e calmas, como pede o manual, em AVIF ou WebP. Imagem do topo com `fetchpriority="high"`; as demais com `loading="lazy"`.
- **Ícones** em SVG com `currentColor`, nas grades de 16, 20 e 24 px e traço de 1,5 ou 2 px.

## Movimento

A web usa os mesmos tokens de movimento propostos para os apps, como variáveis CSS. Movimento é curto, desacelera ao chegar e some quando a pessoa pede menos movimento.

| Token (proposta) | Duração | Uso na web |
| --- | --- | --- |
| `--motion-fast` | 100 ms | Hover, pressionado, troca de cor |
| `--motion-base` | 200 ms | Abrir menu suspenso, dica, abas, transição entre páginas |
| `--motion-screen` | 300 ms | Painel de menu e folha inferior no celular, diálogo |
| `--motion-slow` | 450 ms | Entrada de banner, gráficos que se desenham |

Curvas: entrada `cubic-bezier(0.2, 0, 0, 1)`, saída `cubic-bezier(0.3, 0, 1, 1)`.

- **`prefers-reduced-motion: reduce`:** só mudanças de opacidade; nada se desloca, nada se repete.
- **Sem sequestro de rolagem** e sem parallax. Elementos que aparecem ao rolar só esvanecem e sobem até 16 px, uma vez.
- **Só `transform` e `opacity`** são animados, para manter a página fluida no celular.
- **Painéis:** no celular deslizam da borda; no desktop esvanecem no lugar.
- **Carregamento:** indicador orbital (um ponto percorrendo um arco) ou blocos `surfaceElevated` no lugar do conteúdo. O logo nunca gira.

## Acessibilidade

A meta é WCAG 2.2 nível AA em todas as faixas. Cores e contraste já vêm resolvidos pelo manual; os critérios abaixo dependem de como o layout responde.

| Critério WCAG 2.2 | O que exige | Como a CAPRA cumpre |
| --- | --- | --- |
| 1.4.3 Contraste mínimo | Texto com 4,5:1 ou mais | Só pares de tokens do manual (7:1 no dark, 4,5:1 no claro) |
| 1.4.11 Contraste não textual | Bordas de controles com 3:1 ou mais | Controles com `borderStrong`, nunca só `border` |
| 1.4.4 Redimensionar texto | Texto em 200% sem perda | Tamanhos em `rem`, caixas sem altura fixa |
| 1.4.10 Reflow | Sem rolagem nas duas direções em 320 px de largura, o mesmo que 1280 px com zoom de 400% | Layout base desenhado para 320 px; rolagem horizontal só dentro de tabelas e abas |
| 1.4.12 Espaçamento de texto | Nada se perde com entrelinha 1,5, parágrafos 2×, letras +0,12 em e palavras +0,16 em | Nenhuma caixa de texto com altura fixa |
| 2.4.7 e 2.4.11 Foco visível e não encoberto | Foco visível e não escondido pelo cabeçalho fixo | `focus-ring`; `scroll-padding-top` igual à altura do cabeçalho |
| 2.5.8 Tamanho do alvo (mínimo) | 24 × 24 px ou espaço equivalente | Alvos de 40 px com mouse e de 44 a 48 px com toque |
| 1.3.4 Orientação | Não travar retrato ou paisagem | Nenhuma tela exige orientação |
| 3.1.1 Idioma da página | Idioma declarado | `lang="pt-BR"` no `<html>` |

- **Estrutura:** `header`, `nav`, `main` e `footer` em todas as páginas; títulos em ordem, sem pular nível.
- **Imagens:** logo com texto alternativo; espirais, pontos e ilustrações decorativas com `aria-hidden="true"`.
- **Preferências do sistema:** `prefers-contrast: more` troca `border` por `borderStrong`; `forced-colors` e `prefers-reduced-motion` tratados como nas seções anteriores.
- **Teste** em 320 px, com zoom de 200% e 400%, só com teclado e com leitor de tela no celular e no desktop.

## Implementação e desempenho

`capra-tokens.json` continua sendo a fonte única: dele saem as variáveis CSS da web e o tema Flutter dos apps. Breakpoints e movimento entram no mesmo arquivo quando forem aprovados.

### Técnicas

- **Página por media query, componente por container query.** A grade da página muda com `min-width`; cartões, tabelas e gráficos mudam com `@container`.
- **Meta viewport** `width=device-width, initial-scale=1`; com `viewport-fit=cover`, conteúdo protegido por `env(safe-area-inset-*)` em PWAs.
- **Altura de tela no celular** com `dvh`, não `vh`: as barras do navegador mudam de tamanho ao rolar.
- **Grade** com CSS Grid (`fr`, `minmax`) e margens com as variáveis de espaço; nada de larguras fixas em px no conteúdo.
- **Imagens e logos** com `width` e `height` declarados, para reservar o espaço antes de carregar.
- **Flutter web:** se um produto usar, as mesmas faixas e tokens valem. Sites que dependem de busca e compartilhamento ficam em HTML.

### Metas de desempenho

Medidas no 75º percentil de visitas reais, separadas entre celular e desktop.

| Métrica | Meta | O que mais afeta nos sites CAPRA |
| --- | --- | --- |
| LCP (carregamento do maior elemento) | 2,5 s ou menos | Imagem ou título do banner: sem `loading="lazy"` e com `fetchpriority="high"` |
| INP (resposta à interação) | 200 ms ou menos | Scripts de terceiros e menus pesados no celular |
| CLS (estabilidade do layout) | 0,1 ou menos | Fontes sem `size-adjust`, imagens sem proporção reservada, avisos de cookies que empurram a página |

### Larguras de teste

| Largura × altura (px) | Representa |
| --- | --- |
| 320 × 568 | Mínimo exigido pelo reflow |
| 360 × 800 | Celular Android comum |
| 390 × 844 | iPhone comum |
| 768 × 1024 | Tablet em retrato |
| 1280 × 800 | Notebook |
| 1920 × 1080 | Monitor de desktop |

## Checklist de entrega

Use esta lista antes de publicar cada site ou versão de aplicação web. A última parte reúne as propostas que precisam de aprovação para o manual v1.4.

### Marca

- [ ] Logo do cabeçalho em SVG, nunca abaixo de 120 px, com versão por tema
- [ ] Favicon SVG, PNG de 16, 32 e 48 px, `apple-touch-icon` e ícones do manifesto conferidos
- [ ] Imagem de compartilhamento de 1200 × 630 px com título e marca no centro
- [ ] `theme-color` para os dois temas

### Layout

- [ ] Páginas conferidas nas seis larguras de teste, sem rolagem horizontal da página
- [ ] Navegação com os mesmos destinos e a mesma ordem em todas as faixas
- [ ] Tabelas, diálogos e filtros com a forma de celular abaixo de 840 px
- [ ] Banner recomposto por faixa, sem texto sobre a espiral

### Interação e acessibilidade

- [ ] Hover só com `@media (hover: hover)`; alvos de 44 a 48 px com toque
- [ ] Foco visível e não escondido pelo cabeçalho fixo
- [ ] Zoom de 200% e 400% sem perda de conteúdo
- [ ] Campos com 16 px no celular
- [ ] Movimento reduzido, alto contraste e cores forçadas testados

### Desempenho

- [ ] LCP, INP e CLS dentro da meta no celular e no desktop
- [ ] Fontes auto-hospedadas com `swap` e reserva ajustada
- [ ] Imagens com proporção reservada; imagem do topo sem carregamento tardio

### Aprovar para a v1.4

- [ ] Tokens de breakpoint `bp-xs` a `bp-xl`
- [ ] Alturas de cabeçalho por faixa (56, 64 e 72 px)
- [ ] Escala tipográfica por faixa, com corpo de 16 / 26 em textos longos
- [ ] Tokens de movimento e curvas, comuns a web e apps

## Fontes

- Manual de marca CAPRA v1.3 (`capra-manual-de-marca-v1_3.md`)
- Documento CAPRA: Identidade Visual para Aplicativos Mobile (faixas de largura, escala mobile e movimento)
- [ADA Compliance Pros: critérios novos da WCAG 2.2 e reflow](https://www.adacompliancepros.com/blog/wcag-22-new-criteria-thresholds)
- [Deque University: regra de tamanho de alvo (WCAG 2.5.8)](https://dequeuniversity.com/rules/axe/4.7/target-size)
- [Specification.website: Core Web Vitals](https://specification.website/spec/performance/core-web-vitals/)
- [rgb.ir: metas de Core Web Vitals sem mudança em 2026](https://rgb.ir/en/blog/core-web-vitals-thresholds-2026/)

Os critérios 1.4.12 e 2.4.11, a zona segura de 80% de ícones mascaráveis e o zoom do Safari em campos menores que 16 px vêm de documentação conhecida e não foram reconferidos nesta versão.
