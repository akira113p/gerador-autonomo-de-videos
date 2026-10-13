---
name: feedback-producao-sequencial
description: "Produzir os vídeos do canal um por vez, sem subagentes na produção; terminar, anotar e subir ao YouTube antes do próximo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 266b1105-e311-4866-bfa2-82757d8abac0
  modified: 2026-10-13T07:47:36.833Z
---

Produzir os vídeos em ordem, um de cada vez, 100% (imagens, voz, trilha, montagem, miniatura, descrição, upload privado) e deixar um `NOTAS.md` na pasta do vídeo antes de passar ao próximo.

**Why:** em 2026-10-13 o usuário parou 3 agentes em paralelo e disse que "usar vários agentes pra cada vídeo está comendo muito token". A GPU de 8 GB também só roda uma etapa por vez, então o paralelo não ganha tempo na produção.

**How to apply:** não lançar subagentes por vídeo. Roteiro e checagem de cada vídeo eu faço inline (ou só um agente por vez, se o usuário pedir). Ordem combinada: v8 (Viking, feito), depois os demais. Ver [[imagens-locais]] para o fluxo de imagem (Z-Image primeiro).
