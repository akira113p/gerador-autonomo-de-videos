---
name: project-producao-videos-6-a-11
description: "Estado da produção dos vídeos 6 a 11 (6 temas aprovados em 2026-10-12), pausada em 2026-10-13 com v7 a meio das imagens"
metadata:
  node_type: memory
  type: project
  originSessionId: 266b1105-e311-4866-bfa2-82757d8abac0
  modified: 2026-10-13T18:56:32.354Z
---

Produção pausada pelo usuário em 2026-10-13. Fluxo: um vídeo por vez, 100%, com `NOTAS.md` na pasta e upload privado; ver [[feedback-producao-sequencial]] e [[imagens-locais]].

**Prontos e enviados ao YouTube (privados, falta só o usuário publicar no Studio):**
- v8 `piloto/v8-navio-viking`, https://studio.youtube.com/video/VvlEidUgXBQ/edit
- v6 `piloto/v6-camponesa-medieval`, https://studio.youtube.com/video/Kmr76mYIkMU/edit
- v11 `piloto/v11-oregon-trail`, https://studio.youtube.com/video/cSkp336whPs/edit
Cada um tem `NOTAS.md` com números, lições e fatos a conferir.

**Em andamento: v7 `piloto/v7-pompeia`.** Roteiro, prompts e checagem prontos, scripts já adaptados (BLOCOS, ESTILOS, FALA, descrição, thumb, via `aplicar.py` + `dados_v7.py` no scratchpad da sessão). Imagens: **105 de 183 geradas** (`imagens/`); `gerar_imagens.py` pula as que existem. Falta: terminar imagens, folhas de contato (`folha.py 1 183`) e refazer anacronismos, voz, `conferir.py`, trilhas (`refazer_trilhas.py`), `montar.py`, `gerar_thumb.py`, `gerar_descricao.py`, `publicacao.json`, upload, `NOTAS.md`.

**Ainda não começados:** v9 `piloto/v9-londres-vitoriana` e v10 `piloto/v10-egito-operario`. Roteiro e prompts existem, mas os scripts ainda são do v5 (BLOCOS, ESTILOS, FALA, descrição e thumb por adaptar) e **o v9 não tem arquivo de checagem de fatos** (`pesquisa/checagem-v9-...` não existe). Fazer a checagem antes de dar como pronto.

**Why:** o usuário pausou para controlar custo e tokens (já havia parado os subagentes).
**How to apply:** ao retomar, retomar pelo v7 (subir ComfyUI: `cd C:/ai-local/comfyui && ../venv-comfy/Scripts/python.exe main.py --port 8188`, depois `gerar_imagens.py` da pasta). Ordem de GPU por vídeo: imagens (ComfyUI) → desligar ComfyUI → voz (venv-qwen) + `conferir.py` (venv-voz) → ligar ComfyUI → trilhas → montar → thumb. Não lançar subagentes na produção. Nada está rodando agora.

Lições de prompt que valem para os próximos: navio/estrada/moeda saem modernos se não forem descritos pela forma; cartões com texto longo ou repetido saem errados (usar 1 a 2 palavras); nomes difíceis na voz precisam de grafia fonética sem espaços ("konnistoga", "larremee").
