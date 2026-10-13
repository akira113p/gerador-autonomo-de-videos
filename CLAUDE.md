# Canal dark (faceless): geração de vídeos

Objetivo: renda extra com um canal faceless no YouTube. É um experimento com critério de parada, não um plano de renda garantida.

## Decisões tomadas
- Idioma principal: **inglês**. Dublagem depois em idiomas que pagam bem (faixas de áudio múltiplas).
- Tempo do usuário: **~2 h/semana**. O pipeline precisa ser quase todo automático, mas com autoria real no roteiro (ver política).
- Hardware local: RTX 4060 Laptop (8 GB de VRAM), 16 GB de RAM. Orçamento **US$ 0**: imagem, voz e música só locais ou grátis.
- Cadência: **1 vídeo por dia no mínimo, episódios de ~30 min** (risco de política registrado em docs/decisoes.md). Critério de parada em números: pendente.
- Nicho do piloto: **vida cotidiana histórica** (nicho do canal ainda não fechado).
- Voz do canal: **L6_sereno_leve** (Qwen3-TTS, homem de ~35 anos, leve e natural), referência em `identidade/narrador-leve/`. Escolhida por soar a mais humana entre as testadas.

## Restrições críticas
- Política de conteúdo inautêntico: ver [pesquisa/fase6-politica-youtube.md](pesquisa/fase6-politica-youtube.md). Slideshow genérico de IA + TTS é exemplo oficial de não monetizável.
- Fatos de roteiro histórico precisam de checagem em fonte primária (skill `research`). A IA inventa datas e citações.
- Modelos locais: só licença que permite uso comercial. Detalhes, tamanhos e fontes em [pesquisa/modelos-ia-locais-imagem-audio.md](pesquisa/modelos-ia-locais-imagem-audio.md). Kokoro, Chatterbox, Whisper e Z-Image int8 testados e funcionando (out/2026).

## Modelos de IA locais

Instalados em `C:/ai-local` (D: não tem espaço):
- `comfyui/` + `venv-comfy` (Python 3.12, torch 2.11 cu128): Z-Image Turbo int8 + Qwen3-4B fp8. Subir com `cd C:/ai-local/comfyui && ../venv-comfy/Scripts/python.exe main.py --port 8188`. ~68 s por imagem 1344x768.
- `venv-voz` (Python 3.12, torch 2.6 cu124): Kokoro, Chatterbox, faster-whisper. Executores em `ferramentas/` (`kokoro_run.py`, `chatterbox_run.py`, `whisper_run.py`).
- Prompt de imagem: descrever só o que deve aparecer. Negações ("no sails") fazem o objeto aparecer. Conferir anacronismos em toda imagem.
- Objeto antigo pelo nome sai moderno: "dining couch" vira sofá, "water clock" vira relógio de mostrador, "calendar" vira calendário de espiral, "sundial" vira antena. Descrever a forma (ver tokens em `piloto/v2-dia-em-roma/prompts.py`). Mapa, contagem e número: desenhar em código (`cartoes.py`), porque a IA erra. Texto livre em parede sai como caça-palavras.
- Música: ACE-Step 1.5 turbo no ComfyUI (`acestep_v1.5_turbo` + `qwen_0.6b/1.7b_ace15`, ~1 min por trilha de 3 min). Conferir buracos de silêncio por RMS e refazer com outra seed.
- Voz: palavra latina ou ambígua ("lead", "salutatio") ganha grafia só para a fala no `FALA` do `gerar_voz.py`; maiúsculas e hífens fazem o modelo soletrar.

Candidatos e regras:
- Imagem: Z-Image Turbo (int8/FP8/GGUF); alternativas SDXL + LoRA e FLUX.1 schnell GGUF. Evitar FLUX.1/2 dev (não comercial).
- Voz: Kokoro-82M para narração em inglês; Chatterbox Multilingual e Qwen3-TTS para clonagem/dublagem (testar em pt-BR com teste cego). Evitar XTTS-v2, F5-TTS, Fish Audio S2.
- Transcrição: Parakeet TDT v3 (EN), Whisper large-v3-turbo (outros idiomas).
- Música: biblioteca livre primeiro; ACE-Step 1.5 turbo como alternativa.
- Não usar no OpenMontage com esta GPU: workflow `flux2-txt2img` (NVFP4, 32B), `qwen_image_21` (16 GB), e o padrão SD 2.1 do `local_diffusion`.
- VRAM útil: ~5 GB (o sistema já usa ~2,9 GB). Espaço em disco: ~25 GB (mínimo) a ~65 GB (tudo).

## Estrutura
- `pesquisa/`: notas de pesquisa com fontes.
- `docs/handoff/`: resumo de fim de sessão (skill `handoff`), para retomar na semana seguinte.
- `.claude/skills/`: grill-me, grilling, research, handoff (de mattpocock/skills, MIT; research e handoff adaptados) e duas próprias: `registrar-decisao` (grava decisões em `docs/decisoes.md`) e `retomar-sessao` (lê o estado e propõe o próximo passo; use no começo de cada sessão).
- `docs/decisoes.md`: decisões tomadas e perguntas pendentes.
- `piloto/v1-vindolanda/`: primeiro vídeo piloto (2:02, cartas de Vindolanda, voz `narrador-leve`; a versão anterior com o professor idoso, 2:17, está no commit b405aed/cfa7565). Pipeline em scripts, nesta ordem: `gerar_imagens.py` (venv do OpenMontage, ComfyUI ligado), `gerar_voz.py` (venv-qwen), `conferir.py`, `gerar_trilha.py` e `montar.py` (venv-voz). O `montar.py` gera `piloto_v1.mp4` (AAC, para publicar) e `piloto_v1_vscode.mp4` (Opus: o preview do VS Code não toca AAC e fica mudo). Roteiro, prompts e fontes em `roteiro.json`. Mídia versionada junto.
- `piloto/v2-dia-em-roma/`: primeiro vídeo longo (19:07, "What Did Ancient Romans Actually Do All Day?"). O texto vale em `roteiro.md`; `construir_roteiro.py` gera o `roteiro.json`. Ordem: `gerar_imagens.py` (prompts em `prompts.py`), `cartoes.py` (cartões com número, desenhados em código), `gerar_voz.py`, `conferir.py`, `gerar_trilha.py` (ACE-Step, uma trilha por bloco de capítulos), `montar.py` (imagem parada, sem zoom, crossfade de trilha entre blocos, gera `.srt`), `gerar_descricao.py`, `gerar_thumb.py`.
- `piloto/v3-last-of-us/`: vídeo 3, "What Would YOUR Life Be Like in The Last of Us Apocalypse?" (16:08, enviado como privado em 2026-10-11). Fluxo novo: imagens pelo ChatGPT/Gemini no navegador + plano B local (`gerar_local.py`, Z-Image), voz local (`gerar_voz.py`, `conferir.py`), jazz do 741Hz em outro trecho (`preparar_jazz.py`), `montar.py`, `gerar_thumb.py`, `gerar_descricao.py`, upload com `ferramentas/youtube_upload.py`. Prompts em `prompts.py`; `coletar.py` junta as imagens baixadas. Limites e manhas desse fluxo: `docs/decisoes.md` (2026-10-11).
- `piloto/propostas/`: roteiros dos vídeos 3, 4 e 5 (checagem em `pesquisa/checagem-3-roteiros-propostos.md`). `piloto/v4-futuro-1900/` e `piloto/v5-revolucao-francesa/` têm só o roteiro e os scripts copiados; ainda sem imagens nem voz.
- `piloto/testes-identidade/`: testes de estilo de imagem e de vozes (cópia de `C:/ai-local/piloto`).
- `identidade/`: vozes do canal (referência de clone do Qwen3-TTS): `narrador-leve/` (L6_sereno_leve, **voz atual do canal**), `narrador/` (britânico grave) e `narrador-professor/` (professor idoso), as duas últimas guardadas como alternativas.
- `identidade/pocket-history/`: marca do canal **Pocket History** (foto de perfil 800x800, banner 2048x1152). `gerar_marca.py` gera as bases (venv do OpenMontage, ComfyUI ligado) e `compor_marca.py` recorta, põe o texto e gera as prévias (venv-voz). O texto é sempre por código; o modelo erra letras.
- `ferramentas/`: executores dos modelos locais (rodam no `C:/ai-local/venv-voz`).
- `../openmontage/`: OpenMontage (AGPLv3). Ferramentas adicionadas localmente: `tools/audio/kokoro_tts.py`, `tools/graphics/zimage_image.py`, workflow `tools/_comfyui/workflows/zimage-turbo-txt2img.json` (teste de contrato atualizado com o provedor `kokoro`).
  - venv: `../openmontage/.venv` (Python 3.13; o 3.11 registrado no `py` aponta para um caminho inexistente).
  - Pipelines de interesse: `animated-explainer` (narração + imagens; o do piloto), `documentary-montage` (montagem musical curta, não serve para narração longa), `localization-dub` (dublagem).
  - Não foi instalado: `npx hyperframes` (pacote sem versão fixa) e dependências de GPU (`requirements-gpu.txt`).



vc pode rodar comandos como cd D:\programacao\projetos\videos\openmontage
.\.venv\Scripts\python.exe -m pytest tests/contracts -q
.\.venv\Scripts\python.exe render_demo.py --list