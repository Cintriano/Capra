# CAPRA — Identidade Visual para Apps de TV

Oct 11, 2026 · @Danilo Fernandes

## Introdução

Este documento leva o manual de marca CAPRA v1.3 para apps de TV, vistos a cerca de 3 metros e usados com controle remoto. Ele não muda nenhuma regra do manual: converte medidas para a tela da TV e define foco, navegação e o que entregar às lojas.

| Plataforma | Base técnica | Como aplicar |
| --- | --- | --- |
| Apple TV (tvOS) | App nativo em SwiftUI ou UIKit | Este documento inteiro |
| Google TV e Android TV | App Android, de preferência com Compose for TV | Este documento inteiro |
| Fire TV com Fire OS | App Android | Regras do Android TV |
| TVs Samsung (Tizen) e LG (webOS) | Aplicação web | Este documento, mais o documento web para tokens e implementação |

**Dark first combina com TV.** A sala costuma estar escura e o conteúdo é o protagonista: o fundo Void e os acentos pastel do manual funcionam sem adaptação de paleta.

**Relação com os outros documentos.** Tokens, componentes e movimento vêm do manual e dos documentos de apps mobile e de web. Itens marcados como **proposta** não existem no manual v1.3 e precisam de aprovação para a v1.4.

## Princípios da interface vista a 3 metros

Na TV, o foco é a interface: sempre há um item em foco, ele é visível do sofá e o controle remoto leva a ele de forma previsível. A marca aparece no ícone, na abertura e na cor do foco; o resto da tela é do conteúdo.

- **Maior e com menos coisas.** Cada elemento é lido a 3 metros. Menos itens por tela, mais espaço entre eles.
- **Navegação em quatro direções.** Itens alinhados em fileiras e colunas, para cima, baixo, esquerda e direita levarem ao vizinho óbvio.
- **Voltar sempre volta.** O botão Voltar (Menu nos controles antigos da Apple) desfaz o último passo e, na tela inicial do app, sai dele.
- **Digitar é o último recurso.** Login por código ou QR code no celular, busca por voz e listas de escolha antes do teclado na tela.
- **Calma no escuro.** Dark first, sem grandes áreas brancas que ofuscam na sala escura, sem brilho nem efeitos.
- **Nada que dependa de detalhe fino.** TVs alteram cor, nitidez e contraste: sem linhas de 1 px, sem cinzas quase iguais, sem texto pequeno.

## Tela, unidades e áreas seguras

Regra de conversão: os valores do manual em px valem como dp no Android TV e dobram no tvOS e nas TVs web. Isso funciona porque, a 3 metros, 1 dp numa TV 1080p ocupa no olho mais ou menos o mesmo que 1 pt num celular na mão (aproximação).

|  | tvOS | Google TV e Android TV | TVs web (Tizen, webOS) |
| --- | --- | --- | --- |
| Tela de referência | 1920 × 1080 pt (4K em @2x) | 960 × 540 dp; arquivos pensados para 1080p | 1920 × 1080 px de CSS |
| Margem de segurança | 60 pt em cima e embaixo, 80 pt nas laterais | 48 dp nas laterais e 27 dp em cima e embaixo; textos e informação a 58 e 28 dp | 5%: 96 px nas laterais, 54 px em cima e embaixo (proposta) |
| Grade | Definida pelo layout do app | 12 colunas de 52 dp com 20 dp entre elas | Igual à do Android TV, em dobro |
| Fator sobre o manual | × 2 | × 1 | × 2 |

- **Fundos ocupam a tela toda.** Imagens de fundo e faixas de cor vão até a borda; só texto, foco e controles respeitam a margem.
- **A maioria das TVs modernas não corta mais as bordas**, mas a margem continua: ela também dá respiro para o item em foco crescer.

### Tokens convertidos

| Token | Manual (px) | Android TV (dp) | tvOS (pt) e TV web (px) |
| --- | --- | --- | --- |
| `space-sm` | 8 | 8 | 16 |
| `space-md` | 16 | 16 | 32 |
| `space-lg` | 24 | 24 | 48 |
| `space-xl` | 32 | 32 | 64 |
| `radius-sm` | 8 | 8 | 16 |
| `radius-md` | 12 | 12 | 24 |
| `radius-lg` | 16 | 16 | 32 |
| `icon-size-lg` | 24 | 24 | 48 |

## Layout de referência

A tela inicial típica de um app CAPRA na TV tem um destaque no topo, fileiras de cartões abaixo e o menu lateral recolhido à esquerda.

&#91;embedded content: Tela inicial de referência de um app CAPRA na TV\]

O item em foco é o único elemento com acento na tela, além da seção ativa no menu. As fileiras passam da margem segura até a borda da tela; no tvOS, as medidas dobram em pt e a margem segura é de 80 × 60 pt.

## Ícone, banner e Top Shelf

Na TV, o ícone é retangular e a assinatura completa aparece no banner do Android TV. Tudo continua saindo dos mestres SVG do manual e do gerador de logos filhas.

### Apple TV (tvOS)

| Arquivo | Medidas | Regra CAPRA |
| --- | --- | --- |
| Ícone do app | 400 × 240 e 800 × 480 (@2x), em camadas | Marca centralizada, sem texto |
| Ícone da App Store | 1280 × 768, em camadas | Mesma composição do ícone do app |
| Top Shelf | 1920 × 720, ou 2320 × 720 na versão larga; dobro em @2x | Composição de banner do manual; imagem estática, sem botões desenhados |

O ícone do tvOS é feito de 2 a 5 camadas que o sistema desloca quando ele está em foco. A divisão natural da marca já cria a profundidade, sem efeito desenhado:

| Camada | CAPRA | Logo filha |
| --- | --- | --- |
| Fundo | Cor sólida #121416 | Cor sólida do neutro do produto |
| Meio | Braços do símbolo | Braços |
| Frente | Núcleo | Disco com a letra vazada |

- **Tamanho da marca (proposta):** 64% da altura do ícone (CAPRA) e 68% (logo filha), as mesmas proporções do ícone quadrado.
- **Zona segura:** o ícone em foco cresce e as bordas das camadas são cortadas; a marca fica longe das bordas.

### Google TV e Android TV

| Arquivo | Medidas | Regra CAPRA |
| --- | --- | --- |
| Banner do app (`android:banner`) | 320 × 180 px, recurso xhdpi | Fundo no neutro; assinatura horizontal (CAPRA) ou assinatura do app com marca e nome (produto), centralizada |
| Ícone adaptativo | O mesmo dos apps mobile | Sem arquivo novo |
| Banner da Google Play para TV | 1280 × 720, JPEG ou PNG 24 bits sem transparência | Mesma composição do banner do app, em alta resolução |

- O banner é o único lugar do ecossistema onde a assinatura completa entra no "ícone": é ele que leva o nome do app na tela inicial do Android TV.
- **TVs web (Tizen, webOS):** cada loja pede seus próprios tamanhos. Gere todos a partir dos mesmos mestres, com as mesmas proporções.

## Logo na TV

O logo aparece na abertura e na tela inicial do app; durante a reprodução, sai de cena. Os tamanhos mínimos seguem a regra de conversão: o número do manual em dp no Android TV e em dobro no tvOS e nas TVs web.

| Versão | Android TV (dp) | tvOS (pt) e TV web (px) |
| --- | --- | --- |
| Assinatura horizontal | 120 de largura | 240 |
| Assinatura vertical | 80 de largura | 160 |
| Logotipo | 72 de largura | 144 |
| Símbolo | 24 | 48 |
| Logo filha completa | 32 | 64 |
| Logo filha reduzida (disco e letra) | 16 a 31 | 32 a 63 |

### Onde aparece

- **Abertura:** o sistema mostra o ícone sobre o fundo `background` (ou o neutro do produto). Se o app tiver tela de carregamento própria, ela usa a assinatura vertical (CAPRA) ou a marca com o nome (produto), centralizadas.
- **Tela inicial do app:** assinatura horizontal (CAPRA) ou assinatura do app (produto) no alto do menu lateral ou no canto superior esquerdo, dentro da margem segura. Nas demais telas, só o título.
- **Durante a reprodução:** nenhuma marca fixa sobre o vídeo ou a capa. A marca pode aparecer nos controles do player enquanto eles estão visíveis.
- **Tela Sobre:** assinatura com endosso ("por CAPRA") e a versão do app em `caption` `textSecondary`.

## Cores na TV

A paleta Dark do manual vale sem mudança; o que muda é a cautela, porque cada TV mostra a cor de um jeito. O acento da área é a cor do foco, e o foco nunca depende só de um tom de cinza.

- **Só tema dark (proposta).** A TV é vista em ambiente escuro. No tvOS, o app fixa a aparência escura mesmo com o sistema no claro.
- **Sem branco puro e sem preto puro em grandes áreas.** O manual já usa #E8ECEE para texto e #121416 para fundo, o que evita brilho excessivo e cinzas "lavados" em TVs mal calibradas.
- **Cinzas próximos podem se fundir.** `surface` (#181B1E) e `surfaceElevated` (#202428) quase se igualam em muitas TVs. Agrupe por espaço e, quando precisar de limite, use `borderStrong`.
- **Bordas finas somem.** A borda de 1 px do manual vira 1 dp no Android TV (2 px reais) e 2 pt no tvOS. Nunca use 1 px real.
- **Acento em áreas pequenas.** Preenchimentos grandes em pastel ofuscam no escuro; o acento fica no foco, no botão primário e nos indicadores.
- **Interface em SDR.** Mesmo em TVs HDR, a interface não usa brilho extra; só o vídeo usa HDR.
- **Telas OLED.** Em telas paradas, como o player de música, controles e marca esmaecem depois de alguns minutos sem interação, para não marcar a tela.

## Tipografia

A TV usa a escala digital do manual sem mudar os números: em dp/sp no Android TV e em dobro no tvOS e nas TVs web. O resultado fica próximo dos tamanhos que os próprios sistemas de TV usam.

| Nível | Android TV (dp/sp) | tvOS (pt) e TV web (px) | Peso | Uso |
| --- | --- | --- | --- | --- |
| Display | 40 / 48 | 80 / 96 | Bold 700 | Destaque da tela inicial |
| H1 | 28 / 36 | 56 / 72 | Bold 700 | Título da tela |
| H2 | 20 / 28 | 40 / 56 | Bold 700 | Título de fileira e de seção |
| Body | 14 / 22 | 28 / 44 | Regular 400 | Descrições e textos |
| Rótulo | 14 / 20 | 28 / 40 | Medium 500 | Botões, abas, títulos de cartão |
| Caption | 12 / 16 | 24 / 32 | Regular 400 | Metadados: duração, ano, categoria |

Valores em tamanho / entrelinha. JetBrains Mono não é usada na TV.

- **Mínimo de 12 dp ou 24 pt.** Nada menor, nem em metadados.
- **Peso mínimo Regular 400.** Pesos finos somem a 3 metros.
- **Textos curtos.** Descrição com até 3 linhas na tela de detalhe; textos longos, como termos de uso, vão para uma tela própria com rolagem.
- **Título de cartão** com até 2 linhas; cortado com reticências fora de foco e completo quando o cartão está em foco.
- **Números tabulares** em duração, horário e valores.
- **Caixa de frase** em títulos, botões e menus.

## Foco, navegação e componentes

O foco CAPRA (proposta) é o `focus-ring` do manual ampliado para a TV: o item cresce um pouco, ganha um anel no acento com respiro na cor do fundo e nenhuma sombra ou brilho. Componentes do sistema, como o teclado e os controles padrão do tvOS, mantêm o foco da plataforma.

### Estado de foco

| Propriedade | Android TV (dp) | tvOS (pt) |
| --- | --- | --- |
| Escala do item em foco | 1,05 em botões; 1,1 em cartões | Igual |
| Respiro na cor do fundo | 2 | 4 |
| Anel no acento da área | 2 | 4 |
| Sombra, brilho, halo | Nenhum | Nenhum |

### Controle remoto

- **Direcional:** move um item por vez; segurar rola a fileira. O item em foco fica numa posição fixa à esquerda e a fileira anda por baixo dele.
- **OK / clique:** executa a ação do item. **Voltar:** desfaz o último passo. **Reproduzir/Pausar:** age direto no conteúdo em foco.
- **Pressionar e segurar:** abre ações secundárias, como "Adicionar à lista".
- **Memória de foco:** ao voltar para uma fileira ou tela, o foco retorna ao último item visitado.
- **Foco inicial:** na ação principal da tela ou no primeiro item da primeira fileira.

### Componentes

| Componente | Fora de foco | Em foco |
| --- | --- | --- |
| Botão | `surfaceElevated`, texto `textPrimary`, altura 40 dp (80 pt), `radius-md` | Preenchimento no acento, texto `onAccent`, escala 1,05 |
| Cartão de conteúdo | Imagem com `radius-md`, título abaixo em `textSecondary` | Escala 1,1, anel no acento, título em `textPrimary` e completo |
| Menu lateral | Recolhido, só ícones de 24 dp (48 pt) | Abre com rótulos sobre `surface`; item em foco com fundo no acento e texto `onAccent` |
| Abas no topo | Rótulo em `textSecondary` | Rótulo em `textPrimary` com indicador em pílula no acento |
| Linha de configuração | Altura 48 dp (96 pt), texto `textPrimary` | Fundo `surfaceElevated` e anel no acento |
| Diálogo | Centralizado, `surfaceElevated`, `radius-lg`, no máximo 3 botões | Foco inicial na ação segura, nunca na destrutiva |
| Controles do player | Aparecem ao apertar qualquer botão e somem depois de 5 s | Barra de progresso no acento, tempo com números tabulares |

- **Larguras de cartão:** as da grade do Android TV (124, 196, 268, 412 e 844 dp), em dobro no tvOS.
- **Fileiras:** título em H2 acima, 24 dp (48 pt) entre fileiras, e a fileira seguinte aparece parcialmente na base da tela para mostrar que há mais conteúdo.
- **Teclado na tela:** o do sistema, sem personalização.

## Movimento na TV

A TV usa os tokens de movimento propostos nos documentos de apps e de web. O que manda é a resposta ao controle: o foco anda no instante em que o botão é apertado, e toda animação pode ser interrompida pelo próximo comando.

| Momento | Token (proposta) | Duração |
| --- | --- | --- |
| Foco muda de item (escala e anel) | `motion-base` | 200 ms |
| Fileira rola para acompanhar o foco | `motion-screen` | 300 ms |
| Troca de tela, menu lateral abrindo | `motion-screen` | 300 ms |
| Controles do player aparecendo ou sumindo | `motion-base` | 200 ms |

- **Direcional segurado:** a fileira rola contínua, sem esperar cada animação terminar.
- **Prévia de vídeo automática** (opcional): só depois de 3 s com o item parado em foco, e nunca se o sistema estiver com prévias ou movimento desligados.
- **Carregamento:** indicador orbital, um ponto percorrendo um arco; o logo nunca gira.
- **Profundidade só do sistema:** o deslocamento em camadas do tvOS é da plataforma. O app não desenha parallax nem efeitos 3D próprios.

## Acessibilidade na TV

Na TV, acessibilidade começa pelo foco: tudo que o leitor de tela anuncia, o controle alcança, e tudo que o controle alcança, o leitor anuncia. A paleta já garante o contraste; o resto depende dos recursos do sistema.

| Recurso do sistema | O que o app faz |
| --- | --- |
| Leitor de tela (VoiceOver no tvOS, TalkBack no Android TV) | Anuncia o item em foco com nome, tipo e estado. Cartões têm descrição; espirais e pontos decorativos ficam ocultos |
| Legendas | O player oferece legendas e respeita o estilo escolhido no sistema (tamanho, cor, fundo). Com os controles visíveis, a legenda sobe para não ficar coberta |
| Texto em negrito e tamanho de texto | Onde o sistema oferecer, o app acompanha e o layout cresce sem cortar |
| Aumentar contraste | Divisórias e cartões passam de `border` para `borderStrong` |
| Reduzir movimento | Sem prévias automáticas; o foco mostra só o anel, sem escala |
| Comandos de voz | Ações com verbos claros ("Reproduzir", "Adicionar à lista") e busca por voz |

- **Cor nunca sozinha:** estado sempre com ícone e texto.
- **Sem piscar:** nada pisca mais de 3 vezes por segundo, nem em animações de carregamento.
- **Sem pressa:** nenhuma escolha tem tempo-limite; controles que somem voltam com qualquer botão.

## Materiais para lojas

Na TV, a vitrine é a própria interface em tela cheia: capturas reais, sem moldura de aparelho, com dados fictícios. O banner e o ícone vêm dos mesmos mestres do app.

| Loja | Item | Medidas | Regras |
| --- | --- | --- | --- |
| App Store (Apple TV) | Ícone da App Store | 1280 × 768, em camadas | Vai dentro do app; trocar exige nova versão |
| App Store (Apple TV) | Capturas de tela | 1920 × 1080 ou 3840 × 2160 | JPEG ou PNG sem transparência, 1 a 10 por idioma |
| Google Play | Banner de TV | 1280 × 720 | JPEG ou PNG 24 bits sem transparência; obrigatório para apps de Android TV |
| Google Play | Capturas de TV | 1920 × 1080 recomendado | Pelo menos uma; aparecem só para quem navega pela TV |
| Lojas Samsung e LG | Ícones, banners e capturas | Conforme cada loja | Gerados dos mesmos mestres |

- **Primeira captura:** a tela inicial do app com conteúdo e um item em foco, para mostrar o anel no acento.
- **Sem texto sobreposto** nas capturas de TV: a interface fala sozinha a 3 metros.
- **Dados fictícios** em saldos, nomes e históricos.
- **Top Shelf** segue a composição de banner do manual: fundo Void, espiral recortada, poucos pontos e assinatura pequena. O banner da Google Play repete o banner do app em alta resolução.

## Checklist de entrega

Use esta lista antes de cada versão de app de TV. A última parte reúne as propostas que precisam de aprovação para o manual v1.4.

### Marca

- [ ] Ícone do tvOS em camadas (fundo, braços, frente) e conferido em foco
- [ ] Banner do Android TV de 320 × 180 px com a assinatura no neutro
- [ ] Top Shelf de 1920 × 720 (e 2320 × 720) com a composição de banner
- [ ] Logo dentro dos mínimos da tabela e fora da tela durante a reprodução

### Tela e navegação

- [ ] Texto, foco e controles dentro da margem segura; fundos até a borda
- [ ] Todo item alcançável pelo direcional, com vizinho previsível nas quatro direções
- [ ] Foco visível do sofá em todas as telas, com anel no acento
- [ ] Voltar desfaz o último passo; memória de foco nas fileiras
- [ ] Testado numa TV real, a 3 metros, além do emulador

### Cores, texto e acessibilidade

- [ ] Nenhum texto abaixo de 12 dp ou 24 pt; peso mínimo Regular
- [ ] Nenhuma linha de 1 px real
- [ ] Leitor de tela anuncia o item em foco; legendas seguem o estilo do sistema
- [ ] Controles e marca esmaecem em telas paradas

### Lojas

- [ ] Capturas em 1920 × 1080 ou 3840 × 2160, sem moldura e com dados fictícios
- [ ] Banner de TV de 1280 × 720 na Google Play

### Aprovar para a v1.4

- [ ] Regra de conversão (× 1 em dp no Android TV, × 2 no tvOS e na TV web)
- [ ] Estado de foco CAPRA para TV (escala, respiro e anel)
- [ ] Só tema dark nos apps de TV
- [ ] Margem de 5% para TVs web
- [ ] Tamanho da marca no ícone do tvOS (64% e 68% da altura)

## Fontes

- Manual de marca CAPRA v1.3 (`capra-manual-de-marca-v1_3.md`)
- Documentos CAPRA de apps mobile e de web responsiva (tokens de movimento, regras de componentes)
- [Android Developers: layouts para TV](https://developer.android.com/design/ui/tv/guides/styles/layouts) (tela de 960 × 540 dp, margens, grade e larguras de cartão)
- [Apple: Asset Catalog Format Reference, Brand Assets](https://developer.apple.com/library/ios/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/BrandAssetsType.html) (ícone 400 × 240 e 1280 × 768, Top Shelf)
- [EaselTV: Apple TV submission](https://docs.easeltv.com/docs/apple-tv-submission) (Top Shelf larga e resoluções @2x)
- [Google Play Console Help: Add preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en-GB) (banner de TV e capturas)
- [AxonBuild: App Store screenshot and icon sizes](https://axonbuild.com/blog/app-store-screenshot-and-icon-sizes/) (capturas do Apple TV)

A margem segura do tvOS (60 e 80 pt), o limite de 2 a 5 camadas no ícone do tvOS e o banner de 320 × 180 px do Android TV vêm da documentação das plataformas e não foram reconferidos nesta versão.
