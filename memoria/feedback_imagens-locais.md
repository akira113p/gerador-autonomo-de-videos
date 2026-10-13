---
name: feedback-imagens-locais
description: "Imagens dos vídeos do canal são geradas localmente (Z-Image/ComfyUI), não pelo ChatGPT no browser"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f50d79b1-ee6a-4cde-8595-56ce2d3b3256
  modified: 2026-10-12T05:10:51.400Z
---

Gerar as imagens dos vídeos localmente com Z-Image (ComfyUI), não pelo ChatGPT no browser.

**Why:** em 2026-10-12 o usuário interrompeu o laço que eu havia montado no ChatGPT (via Chrome) e pediu "gere as fotos localmente". O v3 já tinha acabado no plano B local (`gerar_local.py`).

**How to apply:** usar `gerar_imagens.py` de cada piloto (venv do OpenMontage, ComfyUI ligado). Não abrir o ChatGPT para imagem. Ver [[pipeline-video-piloto]] se existir.
