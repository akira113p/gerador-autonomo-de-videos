# Pocket History: pipeline de vídeos para um canal faceless, 100% local e grátis

Um experimento para produzir vídeos longos de YouTube (narração + imagens + música + legendas) quase sem intervenção manual, rodando em um notebook comum (RTX 4060 de 8 GB, 16 GB de RAM) com **orçamento US$ 0**.

O canal se chama **Pocket History**. O formato de maior retorno até agora é "What Would YOUR Life Be Like...?": um universo conhecido (história, jogo, série) narrado em segunda pessoa, com checagem de fatos do mundo real e fontes na descrição.

> **Isto é um experimento com critério de parada, não um plano de renda garantida.** Os números reais do canal (poucos views, CTR de 1,0%) estão em [docs/analise-canal-2026-10-19.md](docs/analise-canal-2026-10-19.md), sem maquiagem.

A documentação do projeto está em português. Os vídeos, a narração e as descrições publicadas são em inglês.

---

## O que o repositório contém

| Parte | O que é |
|---|---|
| **Pipeline de produção** | Scripts Python por vídeo: roteiro → imagens → voz → conferência → trilha → montagem (ffmpeg) → thumbnail → descrição → upload |
| **Modelos de IA locais** | Executores para Kokoro, Chatterbox, Qwen3-TTS (voz), faster-whisper (transcrição) e ComfyUI com Z-Image Turbo / FLUX.2 klein (imagem), em [ferramentas/](ferramentas/) |
| **14 vídeos piloto** | Roteiro, prompts, fontes e scripts de cada um em [piloto/](piloto/) |
| **Pesquisa com fontes** | Política do YouTube, modelos e licenças, retenção, checagem de fatos por vídeo em [pesquisa/](pesquisa/) |
| **Registro de decisões** | Cada escolha com data e motivo em [docs/decisoes.md](docs/decisoes.md) |
| **Skills do Claude Code** | Fluxo de trabalho assistido por IA em [.claude/skills/](.claude/skills/) |

Os vídeos finais (`.mp4`) e os áudios intermediários pesados **não** estão versionados. Os scripts os recriam.

## Como um vídeo é feito

```
roteiro.md ──► construir_roteiro.py ──► roteiro.json
                                            │
        ┌───────────────────────────────────┤
        ▼                                   ▼
  gerar_imagens.py / gerar_local.py     gerar_voz.py ──► conferir.py
  (ComfyUI: Z-Image / FLUX.2 klein,     (Qwen3-TTS, voz        (Whisper compara a fala
   ou ChatGPT no navegador)              "narrador-leve")        com o texto)
        │                                   │
        └──────────────┬────────────────────┘
                       ▼
            cartoes.py (números, mapas, contagens: desenhados em código)
                       ▼
        preparar trilhas / jazz (música livre, "no copyright")
                       ▼
          montar.py (ffmpeg: imagem + voz + trilha + legendas .srt)
                       ▼
     gerar_thumb.py · gerar_descricao.py · youtube_upload.py (envio privado)
```

Principais decisões de projeto:

- **Autoria real no roteiro.** Slideshow genérico de IA com TTS é exemplo oficial de conteúdo não monetizável pela política de "conteúdo inautêntico" do YouTube ([análise](pesquisa/fase6-politica-youtube.md)). Por isso o roteiro tem pesquisa, ponto de vista e checagem em fonte primária; a IA faz a parte mecânica.
- **Checagem de fatos.** Modelos inventam datas e citações. Cada roteiro histórico tem uma nota de checagem em [pesquisa/](pesquisa/) e as fontes vão na descrição.
- **Só licenças que permitem uso comercial.** Evitados: FLUX.1/2 dev, XTTS-v2, F5-TTS, Fish Audio S2. Detalhes em [pesquisa/modelos-ia-locais-imagem-audio.md](pesquisa/modelos-ia-locais-imagem-audio.md).
- **O que a IA erra, o código desenha.** Mapas, contagens, números e texto em imagem saem errados no modelo de imagem; o projeto os gera com Pillow/código.
- **Prompts de imagem sem negação.** "No sails" faz o objeto aparecer; descreve-se só o que deve aparecer. Objetos antigos pelo nome saem modernos ("sundial" vira antena), então descreve-se a forma.
- **Música livre.** Biblioteca "no copyright" ou jazz livre; só entra faixa cujo título ou descrição declare isso.

## Stack

- **Imagem:** ComfyUI + Z-Image Turbo (int8) + Qwen3-4B (fp8), ~68 s por imagem 1344×768; FLUX.2 klein 4B para gerar com imagem de referência ([pesquisa](pesquisa/imagem-local-com-referencia.md)). No primeiro minuto de alguns vídeos, imagens do ChatGPT pelo navegador.
- **Voz:** Qwen3-TTS (clone de referência, voz atual do canal em [identidade/narrador-leve/](identidade/narrador-leve/)), Kokoro-82M e Chatterbox para comparação e dublagem.
- **Transcrição / conferência:** faster-whisper.
- **Montagem:** ffmpeg, com imagem parada, crossfade de trilha entre blocos e legendas `.srt`.
- **Orquestração:** [OpenMontage](https://github.com/calesthio/OpenMontage) (AGPLv3, repositório separado) para o pipeline `animated-explainer`; Claude Code com skills próprias para pesquisa, roteiro e registro de decisões.
- **Hardware de referência:** RTX 4060 Laptop 8 GB (uns 5 GB de VRAM úteis), 16 GB de RAM, Windows 11.

## Vídeos piloto

| Pasta | Tema |
|---|---|
| [v1-vindolanda](piloto/v1-vindolanda/) | Cartas romanas de Vindolanda (curto, teste de identidade) |
| [v2-dia-em-roma](piloto/v2-dia-em-roma/) | What Did Ancient Romans Actually Do All Day? (19 min) |
| [v3-last-of-us](piloto/v3-last-of-us/) | What Would YOUR Life Be Like in The Last of Us Apocalypse? |
| [v4-futuro-1900](piloto/v4-futuro-1900/) | How People in 1900 Imagined the Year 2000 |
| [v5-revolucao-francesa](piloto/v5-revolucao-francesa/) | Daily Life During the French Revolution (1794) |
| [v6-camponesa-medieval](piloto/v6-camponesa-medieval/) | Life as a Medieval Peasant (England, 1300) |
| [v7-pompeia](piloto/v7-pompeia/) | Pompeia |
| [v8-navio-viking](piloto/v8-navio-viking/) | Life on a Viking Ship (Iceland to Greenland, 985) |
| [v9-londres-vitoriana](piloto/v9-londres-vitoriana/) | Londres vitoriana |
| [v10-egito-operario](piloto/v10-egito-operario/) | Operário no Egito antigo |
| [v11-oregon-trail](piloto/v11-oregon-trail/) | Life on the Oregon Trail (1850) |
| [v12-resident-evil](piloto/v12-resident-evil/) | Could YOU Escape Raccoon City? |
| [v13-bloods-nova-york](piloto/v13-bloods-nova-york/) | Life If You Joined the Bloods |
| [v14-backrooms](piloto/v14-backrooms/) | Life in The Backrooms |

Cada pasta tem `roteiro.md`/`roteiro.json`, prompts, scripts e, quando existe, `NOTAS.md` com o que deu certo e errado. Alguns pilotos (v4, v5, v9, v10) pararam na etapa de roteiro/imagens.

## Como rodar (resumo)

Os caminhos assumem a máquina original (modelos em `C:/ai-local`). Adapte-os.

1. **ComfyUI** com Z-Image Turbo: `cd C:/ai-local/comfyui && ../venv-comfy/Scripts/python.exe main.py --port 8188`.
2. **Ambiente de voz** (Python 3.12, torch cu124) com Kokoro, Chatterbox e faster-whisper; os executores estão em [ferramentas/](ferramentas/).
3. Dentro da pasta de um vídeo, na ordem: `gerar_imagens.py` → `gerar_voz.py` → `conferir.py` → trilha → `montar.py` → `gerar_thumb.py` → `gerar_descricao.py`.
4. Para enviar ao YouTube (sempre como privado), [ferramentas/youtube_upload.py](ferramentas/youtube_upload.py) usa OAuth. Crie o seu `client_secret.json` em `ferramentas/.youtube/` (pasta ignorada pelo git; **nunca versione credenciais**).

Não há instalador único: é um projeto de pesquisa, não um produto. Leia [CLAUDE.md](CLAUDE.md) para o estado atual e as restrições.

## Aviso sobre conteúdo e direitos

Parte dos vídeos usa universos de ficção (jogos, séries) como gancho. São produções independentes de fãs, sem afiliação com os detentores dos direitos, e isso é dito nas descrições publicadas. O risco de Content ID e de marca é assumido pelo autor. Música: só faixas declaradas sem direitos autorais. Imagens e vozes são geradas por IA e rotuladas como tal quando a plataforma pede.

## Licenças

- **Código e documentação próprios:** [MIT](LICENSE).
- **Skills de terceiros** em `.claude/skills/`: `grill-me`, `grilling`, `research` e `handoff` vêm de [mattpocock/skills](https://github.com/mattpocock/skills) (MIT, adaptadas); as `yt-*` vêm de [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) (MIT). Licenças originais ao lado delas.
- **Modelos de IA** não estão no repositório; cada um tem a sua licença (resumo em [pesquisa/modelos-ia-locais-imagem-audio.md](pesquisa/modelos-ia-locais-imagem-audio.md)).
- **OpenMontage** é AGPLv3 e fica fora deste repositório.

## Estrutura

```
.claude/skills/        skills do Claude Code (pesquisa, decisões, retomada, yt-*)
docs/                  decisões, análise do canal, retenção, handoffs
ferramentas/           executores dos modelos locais e upload do YouTube
identidade/            vozes de referência e marca Pocket History
memoria/               memória do assistente sobre o projeto
pesquisa/              pesquisas com fontes e checagens de fatos
piloto/                14 vídeos piloto + propostas + testes de estilo
CLAUDE.md              estado atual, decisões e restrições do projeto
```
