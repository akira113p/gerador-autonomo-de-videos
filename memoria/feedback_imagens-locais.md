---
name: feedback-imagens-locais
description: "Fluxo de imagem dos vídeos: primeiro minuto no ChatGPT, resto local (Z-Image ou modelo de edição) usando as imagens do ChatGPT como referência"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a144b20a-2630-4472-8da8-6b0259538767
  modified: 2026-10-19T23:25:25.736Z
---

Desde 2026-10-19: as imagens do **primeiro minuto** de cada vídeo saem do ChatGPT; o **resto** é gerado com IA local **usando as imagens do ChatGPT como referência** (personagem e estilo), não só com prompt de texto.

**Why:** em 2026-10-12 o usuário tinha mandado fazer tudo local ("gere as fotos localmente"); em 2026-10-19 pediu o fluxo misto para os vídeos de franquia (Resident Evil, Bloods, Backrooms): o ChatGPT define o visual do começo, que é o trecho que mais pesa na retenção, e o local mantém o custo zero no resto.

**How to apply:** prompts do primeiro minuto em formato ChatGPT (com `referencia_estilo` anexada, ver [[fluxo-imagens-nuvem]]); o resto em formato de edição por referência ("image 1 = personagem, image 2 = estilo"). Modelo local de referência: ver `pesquisa/imagem-local-com-referencia.md`. Não abrir o ChatGPT para as cenas depois do primeiro minuto.
