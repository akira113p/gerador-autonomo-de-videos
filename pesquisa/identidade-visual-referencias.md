# Identidade visual: dois canais de referência (stickman explainer)

Capturado em 2026-10-08. Frames tirados das sprites de storyboard do YouTube (322x180, 1 frame a cada 5 s no vídeo 1 e a cada 10 s no vídeo 2). Thumbnails em 1280x720. Imagens em [referencias-visuais/](referencias-visuais/).

Limite da captura: storyboard mostra composição, cor e texto, mas não movimento. Transições, zoom/pan e ritmo de corte precisam ser vistos no player.

## Os vídeos

| | Vídeo 1 | Vídeo 2 |
|---|---|---|
| Link | https://www.youtube.com/watch?v=49_Ph2q6uIM | https://www.youtube.com/watch?v=t-0AOC9EMt8 |
| Canal | Ink Explainer | Diário Nada Normal |
| Título | What Did Ancient Humans Do All Day? (exibido em PT por tradução automática) | Como os egípcios conseguiram suportar um calor de 50°C sem eletricidade? |
| Idioma original | Inglês (com dublagem automática em PT) | Português |
| Duração | 11:12 | 38:18 |
| Views | 11,67 mi | 15 mil (publicado em 2026-10-07, um dia antes da captura) |
| Descrição | Lista de fontes primárias (Richard Lee 1968, Sahlins 1972, Suzman, Wiessner 2014) | Texto de documentário, cita Deir el-Medina, vestido de Tarkhan |

O vídeo 2 copia o formato do vídeo 1 (ou do mesmo gênero): stickman, história antiga do cotidiano, roteiro com fontes.

## Identidade comum

- **Personagem**: stickman de cabeça grande, redonda e branca, contorno preto grosso, olhos de ponto ou oval, boca de traço. Corpo de linha simples. Emoção vem só de sobrancelha, olho e boca (suor, lágrima, "?" e "!" flutuando).
- **Traço**: linha preta irregular, estilo caneta/marcador, sem sombra dura. Cor chapada com textura leve de lápis/aquarela.
- **Cenário**: ilustrado e colorido quando narra cena; fundo branco liso quando explica conceito.
- **Alternância de dois tipos de quadro**:
  1. Cena: personagem no ambiente (savana, aldeia, Nilo, interior de casa).
  2. Cartão explicativo: fundo branco, um objeto ou diagrama simples, texto curto manuscrito em caixa alta ("REWIND 50,000 YEARS", "15–20 HOURS ✓✓✓", "CULTURE WAS BORN HERE").
- **Recursos gráficos recorrentes**: X vermelho grande riscando algo (negação), check verde, pin vermelho de mapa, setas manuscritas, tela dividida com linha tracejada (YOU | HIM, FAST | STEADY), mapas políticos com cores chapadas saturadas, linha do tempo com dois pins.
- **Ponte presente/passado**: abre com o espectador moderno (despertador, escritório, ar-condicionado) e volta a ele no fim. Funciona como gancho e fechamento.
- **Thumbnail**: personagem em close com expressão exagerada à esquerda, cena colorida, texto amarelo grosso com contorno preto no topo (2–3 palavras). Céu e cor muito mais saturados que o vídeo.

## Diferenças entre os dois

| | Ink Explainer | Diário Nada Normal |
|---|---|---|
| Paleta do vídeo | Mais saturada: céu azul-turquesa, chão ocre/terra, fogo laranja, noite azul-marinho | Dessaturada, tons de areia, bege, verde-acinzentado, azul-pálido |
| Personagem | Recorrente e fixo: o "homem das cavernas" de cabelo castanho bagunçado e roupa de pele; um pesquisador de chapéu safári | Sem personagem fixo; stickmen genéricos com roupas egípcias, troca de estilo entre quadros |
| Consistência | Alta. Mesmo traço, mesma proporção, mesma tipografia em todo o vídeo | Baixa. Moldura aparece e some, alguns quadros parecem quadrinho, outros pintura, um close de mulher em estilo diferente |
| Texto na tela | Frequente, curto, sempre a mesma fonte manuscrita | Quase nenhum |
| Marca d'água | Ícone pequeno de lâmpada no canto inferior direito de todo quadro | Nenhuma visível |
| Ritmo (estimado) | Imagem nova a cada ~5 s ou menos | Imagem nova a cada ~10 s |

Leitura: a consistência do personagem e os cartões de texto são o que separa o canal grande do imitador. O vídeo 2 parece geração de imagem por prompt sem controle de estilo.

## Paleta extraída (quantização dos frames)

Vídeo 1 (Ink Explainer), por área ocupada:
`#ffffff` branco de cartão 24% · `#b7dcda` céu 9% · `#cebb93` areia 9% · `#c79c68` ocre 8% · `#684b38` pele/cabelo 7% · `#000000` linha 7% · `#85694f` terra 6% · `#ebdfc0` creme 5% · `#2d2928` noite 4%

Destaques (só pela leitura visual, área pequena): vermelho do X e dos pins ~`#e03030`, verde do check ~`#3aa845`, laranja do fogo e pôr do sol ~`#f08a3c`, amarelo da thumbnail ~`#ffee00`.

Vídeo 2 (Diário Nada Normal):
`#d7ccb5` areia 11% · `#feffff` branco 10% · `#beb7a6` pedra 9% · `#dce3db` verde-cinza claro 8% · `#ece6d6` creme 7% · `#c0d3d1` azul-pálido 6% · `#555049` sombra 6% · `#0a0d0f` linha 5%

## Implicações para o canal

- Esse estilo é imagem de IA + narração. O que o salva da regra de conteúdo inautêntico ([fase6-politica-youtube.md](fase6-politica-youtube.md)) é roteiro com fontes, um quadro diferente para cada frase e cartões de texto que fazem parte da explicação. Slideshow genérico com o mesmo visual continua não monetizável.
- O Ink Explainer confirma o modelo decidido: original em inglês, com faixa dublada (o título e o áudio chegaram em PT).
- Para reproduzir com consistência localmente, o ponto difícil é manter o mesmo personagem entre centenas de quadros. Isso pede LoRA de personagem ou imagem de referência (IP-Adapter), não só prompt. Ver [modelos-ia-locais-imagem-audio.md](modelos-ia-locais-imagem-audio.md).
- O gênero está ficando lotado: o vídeo 2 é de um canal que imita o formato e tem 15 mil views no primeiro dia.
