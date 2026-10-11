# CAPRA — Identidade Visual para Dashboards

Oct 11, 2026 · @Danilo Fernandes

## Introdução

Este documento define como os dashboards da CAPRA usam a identidade visual: grade, indicadores, paleta de dados, gráficos, tabelas, filtros e estados. Ele estende o manual v1.3 e pede duas exceções a ele, descritas em Mudanças propostas no manual.

| Tipo de painel | Exemplos | Foco |
| --- | --- | --- |
| Painel de dados | DW\_APOLO | Exploração, comparação, tendências |
| Painel financeiro | Visão de saldos e gastos no Ravix | Valores, variação, metas |
| Painel operacional | Status de automações e infraestrutura | Estados, alertas, tempo real |

| Plataforma | Documento base | O que muda |
| --- | --- | --- |
| Web (desktop e tablet) | Web responsiva | Referência deste documento |
| Celular | Apps mobile e web responsiva | Uma coluna, gráficos simplificados, tabelas viram cartões |
| Relógio e TV | Mobile e TV | Sem dashboard: só um indicador por tela ou complicação |

Itens marcados como **proposta** não existem no manual v1.3 e precisam de aprovação para a v1.4.

## Princípios de dashboard

O manual já dá a regra central: a estrutura vem de espaçamento, hierarquia e agrupamento, e os acentos são sinais de leitura. Um dashboard CAPRA é cinza por padrão e colorido só onde há algo a notar.

- **Leitura em camadas.** No topo, os indicadores dizem o quê; no meio, os gráficos dizem quando e por quê; na base, a tabela dá o detalhe.
- **Cada cartão responde a uma pergunta.** O título diz o que é medido e o período aparece logo abaixo, em `caption`.
- **Cor com significado.** Estado antes de decoração, como diz o manual. Séries secundárias e contexto ficam em tons neutros.
- **Estrutura por espaço, não por caixas.** Cartões discretos, bordas finas, nenhuma sombra.
- **Número primeiro.** Valor grande, unidade, período e comparação, nessa ordem.
- **Gráficos honestos.** Barras começam no zero; eixo cortado só com aviso; gráficos lado a lado usam a mesma escala quando são comparados.
- **Dark first.** Gráficos sobre fundo neutro, nos dois temas.

## Anatomia

Todo painel tem cinco partes, sempre nesta ordem: cabeçalho com período e atualização, filtros, indicadores, gráficos e tabela.

&#91;embedded content: Anatomia de um painel CAPRA no desktop e no celular\]

No celular, os indicadores ficam 2 por linha, os filtros entram num botão e a tabela vira lista de cartões. Só a série em destaque e as variações dos indicadores usam cor.

## Grade e responsividade

O painel usa as faixas de largura do documento web e uma grade de 12, 8 ou 4 colunas. Cada cartão tem um tamanho fixo em colunas por faixa; a ordem de leitura é a mesma em todas as larguras.

| Cartão (proposta) | Desktop, 840 px ou mais (12 col.) | Tablet, 600 a 839 px (8 col.) | Celular, até 599 px (4 col.) | Altura do gráfico |
| --- | --- | --- | --- | --- |
| Indicador | 3 colunas (4 por linha) | 4 colunas (2 por linha) | 2 colunas (2 por linha); 4 se o número for longo | — |
| Gráfico pequeno | 4 colunas (3 por linha) | 4 colunas | 4 colunas | 200 px |
| Gráfico médio | 6 colunas (2 por linha) | 8 colunas | 4 colunas | 280 px |
| Gráfico grande e tabela | 12 colunas | 8 colunas | 4 colunas | 360 px |

- **Espaço entre cartões:** 16 px (`space-md`) no celular, 24 px (`space-lg`) a partir de 600 px.
- **Linhas alinhadas:** cartões da mesma linha têm a mesma altura.
- **Ordem no celular:** a mesma do desktop, da esquerda para a direita e de cima para baixo, com os indicadores primeiro.
- **Densidade:** a primeira tela do painel tem até 4 indicadores e até 6 gráficos. O resto vai para abas ou páginas de detalhe.
- **Cada gráfico se adapta à própria largura** (container query): abaixo de 360 px, a legenda vira rótulo direto na linha e o eixo mostra menos marcas.

## Indicadores (KPIs)

O cartão de indicador mostra um número, sua unidade, o período e a comparação, sem acento no valor. A cor aparece só na variação, e só quando o indicador declara se subir é bom ou ruim.

### Anatomia

| Parte | Estilo |
| --- | --- |
| Rótulo | `caption` em `textSecondary`, caixa de frase: "Receita do mês" |
| Valor | H1 Bold em `textPrimary`, números tabulares. Display só quando o painel tem um único indicador principal |
| Unidade | H2 em `textSecondary`, junto do valor: "R$", "%", "ms" |
| Variação | `caption` Medium: seta, sinal, valor e a base da comparação em `textSecondary` ("vs. setembro") |
| Minigráfico (opcional) | Linha de 1,5 px em `textSecondary`, 24 px de altura, último ponto no acento |
| Meta (opcional) | Barra de 4 px: trilho `surfaceElevated`, preenchimento no acento; ao atingir, `success` com ícone |

### Cor da variação (proposta)

Cada indicador declara uma direção no cadastro: "subir é bom", "subir é ruim" ou "neutro".

| Direção declarada | Subiu | Caiu |
| --- | --- | --- |
| Subir é bom (receita, usuários ativos) | `success`, seta para cima | `danger`, seta para baixo |
| Subir é ruim (custo, erros, tempo de resposta) | `danger`, seta para cima | `success`, seta para baixo |
| Neutro (volume, contagem) | `textSecondary`, seta para cima | `textSecondary`, seta para baixo |

- **Estável:** variação abaixo do limite definido para o indicador aparece em `textSecondary` com o texto "estável".
- **Cor nunca sozinha:** sempre seta, sinal e valor. No Ravix, valores negativos seguem a regra do documento mobile: `danger` com o sinal "−".
- **Clique ou toque** no indicador leva ao detalhe ou aplica o filtro correspondente.

## Paleta de dados

A paleta de dados usa só cores que já existem no manual (proposta). O padrão é o modo destaque: uma série no acento e as demais em cinza; o modo categórico, com até 4 cores, é a exceção.

Os cinco pastéis do manual têm quase a mesma luminosidade: entre si, o contraste fica entre 1,03:1 e 1,33:1. Eles se distinguem só pelo matiz, o que falha para quem tem daltonismo. Por isso: poucas cores, rótulos diretos e nunca cor como único sinal.

### Modo destaque (padrão)

| Papel | Dark | Light | Contraste sobre `surface` (dark / light) |
| --- | --- | --- | --- |
| Série em destaque | Acento do produto | Acento do produto (Light) | 7,6:1 ou mais / 5,6:1 ou mais |
| Demais séries e contexto | `borderStrong` #68737A | `borderStrong` #7E8990 | 3,56:1 / 3,58:1 |

### Modo categórico (até 4 séries)

A série principal usa o acento do produto; as outras seguem a ordem abaixo, pulando a que já foi usada.

| Ordem | Cor | Dark | Light | Contraste sobre `surface` (dark / light) |
| --- | --- | --- | --- | --- |
| 1 | Cyan | #8FB8C5 | #3B6A79 | 8,10:1 / 5,96:1 |
| 2 | Lilac | #B3A6C9 | #665789 | 7,59:1 / 6,38:1 |
| 3 | Peach | #D7AFA3 | #93503E | 8,69:1 / 6,07:1 |
| 4 | Gold | #D6C58F | #776220 | 10,08:1 / 5,91:1 |
| Quinta em diante | "Outros", em `borderStrong` | #68737A | #7E8990 | 3,56:1 / 3,58:1 |

- **Mint fica fora das séries.** Ele é `success` e quase não se distingue do Cyan (1,03:1).
- **Cores de estado não pintam séries.** Em gráficos, estado aparece como linha de referência, faixa ou anotação, sempre com ícone e texto.
- **A mesma categoria tem sempre a mesma cor** em todos os gráficos do painel.

### Escala sequencial (intensidade, mapa de calor)

Mistura de `surfaceElevated` até o acento, em 5 passos. Valores calculados por mistura linear; o exemplo usa Cyan.

| Passo | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Dark | #313A40 | #47585F | #5D757E | #73939E | #8FB8C5 |
| Light | #CED8DC | #ABBEC5 | #89A4AE | #668A96 | #3B6A79 |

Os passos 1 e 2 ficam abaixo de 3:1 sobre `surface`: o valor de cada célula precisa estar escrito ou na dica.

### Escala divergente (acima e abaixo de uma referência)

Peach abaixo, neutro no centro, Cyan acima: o eixo quente e frio continua legível para a maioria dos tipos de daltonismo.

| Passo | Muito abaixo | Abaixo | Referência | Acima | Muito acima |
| --- | --- | --- | --- | --- | --- |
| Dark | #D7AFA3 | #80706C | #2A3035 | #5C747D | #8FB8C5 |
| Light | #93503E | #B2948C | #D0D7DB | #86A0AA | #3B6A79 |

A escala divergente não diz se o desvio é bom ou ruim. Quando houver juízo, use a regra de cor da variação dos indicadores.

## Tipos de gráfico

O tipo de gráfico vem da pergunta que o cartão responde, não do dado disponível. Se a resposta é um número exato, o cartão é um indicador ou uma tabela, não um gráfico.

| Pergunta do cartão | Gráfico | Cuidados |
| --- | --- | --- |
| Como isso evoluiu no tempo? | Linha | Barras verticais quando são até 12 períodos fechados (meses do ano) |
| Qual item é maior? | Barras horizontais, ordenadas do maior para o menor | Rótulos longos cabem sem girar o texto |
| Como um total se divide? | Barra única 100% empilhada | Pizza ou rosca só com até 3 partes |
| Como a composição mudou no tempo? | Área ou barras empilhadas | Até 4 séries; a mais importante embaixo, junto do eixo |
| Estamos na meta? | Barra com marca de meta | Nunca velocímetro |
| Como os valores se distribuem? | Histograma | Faixas de mesma largura |
| Duas medidas têm relação? | Dispersão | Eixos rotulados com unidade |
| Onde há concentração (dia × hora)? | Mapa de calor | Escala sequencial, valor na dica |
| O que levou um total de A a B? | Cascata | Aumentos e reduções com sinal, não só cor |
| Quantos passam de etapa em etapa? | Funil em barras horizontais | Taxa de conversão entre as etapas |

### Evitar

- Gráficos 3D, sombras e gradientes em barras ou fatias.
- Pizza com mais de 3 partes; compare com barras.
- Dois eixos verticais no mesmo gráfico; use dois gráficos com o mesmo eixo de tempo.
- Velocímetros e mostradores; use barra com meta.
- Mapas coloridos por área quando o tamanho da região distorce a leitura; prefira barras por região.
- Animação contínua ou em repetição.

## Estilo dos gráficos

O gráfico CAPRA é quase todo neutro: grade discreta, rótulos em `textSecondary` e cor só nos dados. O último valor de uma linha ganha um ponto, como os pontos orbitais do símbolo.

| Elemento | Especificação (proposta) |
| --- | --- |
| Fundo | O do cartão (`surface`); o gráfico não tem fundo próprio |
| Título e subtítulo | Título em H2; período e unidade em `caption` `textSecondary` logo abaixo |
| Eixo base (zero) | 1 px em `borderStrong` |
| Grade | Só horizontal, 3 a 5 linhas de 1 px em `border` |
| Rótulos de eixo | `caption` em `textSecondary`, números tabulares, abreviados: "1,2 mil", "3,4 mi", "out" |
| Linhas | 2 px na série em destaque, 1,5 px nas demais, pontas e junções arredondadas |
| Pontos | Só no último valor e no ponto em foco, raio de 3 a 4 px |
| Período anterior | Mesma cor da série, linha tracejada de 1,5 px |
| Barras | Cerca de 60% do espaço da categoria, raio de 2 px só na ponta do valor, 4 px entre barras agrupadas, sem contorno |
| Áreas | Cor da série a 24% de opacidade, com linha de 2 px no topo |
| Rótulo de valor | Só no destaque (último valor, máximo); em barras horizontais com até 8 itens, em todas |
| Legenda | De preferência rótulo direto no fim da linha. Se precisar de legenda, acima do gráfico, à esquerda, com marcador circular de 8 px |
| Linha de referência (meta, média) | 1 px tracejada em `textSecondary`, com rótulo na ponta direita |
| Anotação | `caption` em `textSecondary` ligada ao ponto por um fio de 1 px; no máximo 2 por gráfico |
| Dica ao passar ou tocar | `surfaceElevated`, borda `border`, `radius-sm`; data em `caption`, valores em Body tabular com o marcador da série; linha vertical de 1 px em `borderStrong` |

- **Números em português do Brasil:** 1.234,56; R$ 1,2 mil; 12,5%.
- **Sem gradiente, sombra ou brilho** em qualquer parte do gráfico. Os gradientes do manual ficam nos banners.

## Tabelas de dados

Tabelas são para valores exatos e listas para agir. Elas seguem o cartão do manual: fundo `surface`, divisórias finas, sem listras e sem sombra.

| Elemento | Especificação (proposta) |
| --- | --- |
| Cabeçalho | `caption` Medium em `textSecondary`, caixa de frase, fixo ao rolar, divisória de 1 px em `borderStrong` |
| Linhas | Altura de 48 px (padrão), 40 px (densa) ou 56 px (confortável), escolhida pela pessoa; divisória de 1 px em `border` |
| Texto | Alinhado à esquerda |
| Números | Alinhados à direita, tabulares, mesma quantidade de casas decimais na coluna |
| Códigos e IDs | JetBrains Mono 12 / 18 |
| Linha sob o cursor | Fundo `surfaceElevated` |
| Linha selecionada | Fundo `surfaceElevated` e barra de 2 px no acento à esquerda |
| Ordenação | Seta de 16 px no cabeçalho; coluna ordenada com rótulo em `textPrimary` |
| Estado na célula | Badge do manual, com ícone e texto |
| Barra na célula (opcional) | Barra horizontal de 4 px em `borderStrong` atrás do número, proporcional ao valor |
| Linha de total | Bold, com divisória de 1 px em `borderStrong` acima |

- **Primeira coluna fixa** quando a tabela rola na horizontal.
- **Contagem visível:** "1–50 de 1.234", com paginação no desktop e "Carregar mais" no celular.
- **No celular,** tabelas com mais de 4 colunas viram uma lista de cartões, como no documento web.

## Filtros, período e atualização

O período é o filtro mais importante e vem sempre primeiro. Todo painel diz, sem precisar abrir nada, qual período está mostrando e quando os dados foram atualizados.

### Filtros

- **Barra de filtros** logo abaixo do título do painel: período primeiro, depois as dimensões (produto, região, conta).
- **Período com atalhos:** Hoje, 7 dias, 30 dias, Este mês, Personalizado. Ao lado, a opção "Comparar com o período anterior".
- **Filtros ativos** como chips (`radius-sm`, `surfaceElevated`, borda `borderStrong`) com botão de remover e um "Limpar filtros" no fim.
- **Escopo claro:** filtros valem para todos os cartões. Um cartão com filtro próprio mostra ícone e a descrição do filtro no subtítulo.
- **No celular:** o período fica visível como chip; as demais opções abrem num botão "Filtros (3)".
- **Na web,** filtros e período ficam no endereço da página, para o painel poder ser compartilhado como está.

### Atualização

| Situação | Como aparece |
| --- | --- |
| Dados atualizados | "Atualizado às 14:32" em `caption` `textSecondary` no cabeçalho, com botão de atualizar |
| Tempo real | Badge "Ao vivo" na cor `info`, com ponto fixo (sem pulsar) |
| Dados atrasados | Badge `warning` com ícone: "Dados de 3 h atrás" |
| Fuso horário diferente do da pessoa | Fuso indicado ao lado do horário: "14:32 (UTC)" |

## Estados

Um cartão nunca some nem muda de tamanho por falta de dado: ele mantém o título e explica o que houve. As mensagens seguem a regra de escrita do manual, dizendo o que aconteceu e como resolver, sem pedir desculpas.

| Estado | Indicador | Gráfico | Tabela |
| --- | --- | --- | --- |
| Carregando | Bloco `surfaceElevated` no lugar do número | Eixo base e blocos no lugar das marcas | Linhas com blocos no lugar do texto |
| Sem dados no período | "—" e "Sem dados neste período" | Eixo base e a mensagem centralizada, com "Mudar período" | Mensagem e ação no lugar das linhas |
| Erro ao carregar | Ícone, "Não foi possível carregar a receita" e "Tentar de novo" | Igual | Igual |
| Período em andamento | Valor com "até agora" | Último ponto ou barra tracejado, com rótulo "parcial" | Linha marcada como parcial |
| Projeção | Valor com "previsto" | Linha tracejada em `textSecondary` depois do último dado real | Coluna separada "Previsto" |
| Sem permissão | Ícone de cadeado e "Você não tem acesso a estes dados", com quem pode liberar | Igual | Igual |

- **Zero não é ausência.** Zero é um dado e aparece como 0. Dado ausente aparece como "—" e, na linha, como uma interrupção: nunca ligue pontos por cima da falta de dado nem desenhe zero no lugar.
- **Sem brilho animado** nos blocos de carregamento: blocos estáticos ou com variação lenta de opacidade, e nada se mexe com movimento reduzido.
- **O tamanho do cartão é reservado** desde o carregamento, para o painel não pular quando os dados chegam.

## Interação

Todo gráfico funciona com mouse, toque e teclado, e todo valor desenhado pode ser lido como número. As ações de cada cartão ficam num menu "Mais opções" no canto superior direito.

| Entrada | Comportamento |
| --- | --- |
| Mouse | Passar sobre o gráfico mostra a dica e a linha vertical; passar sobre uma série ou legenda deixa as outras em `borderStrong` |
| Toque | Tocar fixa a dica; arrastar sobre a linha percorre os valores; tocar fora fecha |
| Teclado | O gráfico recebe foco; setas andam entre os pontos com a dica junto; Enter abre o detalhe |

- **Detalhamento:** clicar numa barra, ponto ou linha da tabela abre a visão filtrada daquele item, com trilha para voltar.
- **Legenda clicável:** mostra ou oculta séries; pelo menos uma continua visível.
- **Recorte de tempo:** no desktop, arrastar sobre o eixo seleciona um intervalo; no celular, só pelo filtro de período.
- **Menu "Mais opções"** do cartão: Ver como tabela, Exportar CSV, Exportar imagem, Copiar link, Tela cheia.
- **Imagem exportada (proposta):** inclui título, período, fonte dos dados e a assinatura do produto pequena no rodapé, no tema ativo ou no claro para impressão.

## Acessibilidade de dados

Todo gráfico tem três camadas de leitura: o desenho, uma frase com a conclusão e uma tabela com os valores. Quem não enxerga o desenho chega à mesma informação pelas outras duas.

- **Frase de conclusão** como texto alternativo: "Receita subiu 12% em outubro, o maior valor do ano", e não "Gráfico de receita".
- **"Ver como tabela"** em todo gráfico, com os mesmos valores e unidades.
- **Indicadores lidos por inteiro:** "Receita do mês, R$ 120 mil, subiu 12% em relação a setembro".
- **Cor nunca sozinha.** No modo categórico, cada série tem rótulo direto e um marcador diferente (círculo, quadrado, triângulo, losango); comparações usam traço tracejado.
- **Contraste de 3:1** para marcas de gráfico sobre o fundo (WCAG 1.4.11): a paleta passa, exceto os dois primeiros passos da escala sequencial, que sempre têm o valor escrito ou na dica.
- **Daltonismo:** teste cada painel com simulação de deuteranopia e protanopia. Os pastéis do manual se confundem nessas simulações, por isso o limite de 4 séries.
- **Zoom de 200%:** rótulos que se sobrepõem são escondidos por ordem de importância, nunca sobrepostos.
- **Movimento reduzido:** gráficos aparecem já desenhados, sem animação de entrada.

## Mudanças propostas no manual v1.4

Duas regras do manual v1.3 precisam de exceção para dashboards; as demais mudanças são acréscimos. Nenhuma cor nova entra na paleta.

| Regra no v1.3 | Mudança proposta | Motivo |
| --- | --- | --- |
| "Uma cor principal por visualização" | Continua como padrão (modo destaque). Exceção: até 4 cores no modo categórico, na ordem Cyan, Lilac, Peach, Gold | Gráficos com várias séries são comuns em painéis |
| "No máximo dois acentos de contexto na mesma interface" e "o acento identifica o produto" | Dentro de gráficos, os acentos são cores de série e não identificam produto | Um painel do DW\_APOLO pode comparar séries sem sugerir produtos diferentes |
| Sem regra | Mint fora das séries de gráfico | Ele é `success` e se confunde com Cyan |
| Sem regra | Tokens `data-1` a `data-4`, `data-other`, escala sequencial e escala divergente | Implementação igual na web e no Flutter |
| Sem regra | Cada indicador declara se subir é bom, ruim ou neutro; a cor da variação segue essa declaração | Queda nem sempre é ruim, como em custos |

**Nos outros documentos,** nada precisa ser reescrito. Os documentos mobile e web passam a remeter a este para painéis; o de TV continua sem dashboard.

## Checklist de entrega

Use esta lista antes de publicar cada painel ou mudança grande num painel.

### Estrutura

- [ ] Indicadores no topo, gráficos no meio, tabela na base
- [ ] Até 4 indicadores e 6 gráficos na primeira tela
- [ ] Cartões nos tamanhos da grade, com altura reservada desde o carregamento
- [ ] Período e horário de atualização visíveis sem abrir nada

### Dados e cor

- [ ] Modo destaque por padrão; no máximo 4 cores no modo categórico, sem Mint
- [ ] Mesma categoria com a mesma cor em todo o painel
- [ ] Cada indicador com direção declarada (subir é bom, ruim ou neutro)
- [ ] Barras começando no zero; gráficos comparados com a mesma escala
- [ ] Zero e dado ausente diferenciados

### Acessibilidade e interação

- [ ] Frase de conclusão e "Ver como tabela" em todo gráfico
- [ ] Gráficos navegáveis por teclado e por toque
- [ ] Painel testado com simulação de daltonismo e com zoom de 200%
- [ ] Revisado nos temas dark e claro

### Aprovar para a v1.4

- [ ] Exceções às regras de "uma cor por visualização" e de "dois acentos por interface"
- [ ] Tokens da paleta de dados e das escalas sequencial e divergente
- [ ] Regra de cor da variação por direção declarada
- [ ] Tamanhos de cartão e alturas de gráfico

## Fontes

- Manual de marca CAPRA v1.3 (`capra-manual-de-marca-v1_3.md`): paleta, contraste, cartões, badges e princípios de dados
- Documentos CAPRA de apps mobile, web responsiva e apps de TV
- Contrastes calculados com a fórmula de luminância relativa da WCAG a partir dos HEX do manual; escalas sequencial e divergente calculadas por mistura linear entre tokens
