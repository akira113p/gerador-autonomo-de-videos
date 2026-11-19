---
name: feedback-producao-sequencial
description: "Produção dos vídeos um por vez sem subagentes; mas a pesquisa de roteiro pode usar subagentes Sonnet/Haiku em paralelo, com o Opus auditando e escrevendo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a144b20a-2630-4472-8da8-6b0259538767
  modified: 2026-10-20T01:04:53.911Z
---

Produzir os vídeos em ordem, um de cada vez, 100% (imagens, voz, trilha, montagem, miniatura, descrição, upload privado) e deixar um `NOTAS.md` na pasta do vídeo antes de passar ao próximo. Na produção, sem subagentes.

Exceção (2026-10-19): para **pesquisa de roteiro**, o usuário pediu subagentes **Sonnet em paralelo** (um por tema), podendo usar **Haiku** em buscas simples; o Opus (sessão principal) audita as fontes e escreve os roteiros.

**Why:** em 2026-10-13 o usuário parou 3 agentes em paralelo na produção ("comendo muito token"); a GPU de 8 GB só roda uma etapa por vez. Em 2026-10-19 interrompeu a pesquisa que eu fazia inline e pediu "designe subagentes pra fazer a pesquisa, agentes sonnet em paralelo, o opus audita e escreve".

Atualização (2026-10-19, mais tarde): **divisão de papéis**. Agentes Sonnet rodam os comandos de geração, olham as imagens e geram (ChatGPT e local); o Opus só revisa os roteiros e monta o vídeo (edição e mixagem). Vídeos em sequência, mas cada vídeo pode ter vários agentes de níveis diferentes.

**How to apply:** pesquisa e checagem de fatos → subagentes com `model: sonnet` (ou `haiku` para listas/metadados), cada um gravando um `pesquisa/*.md`; eu confiro as afirmações-chave na fonte antes de usar. Geração e conferência de imagens (ChatGPT e local) → agentes Sonnet, uma etapa de GPU por vez. Revisão de roteiro, edição e mixagem → Opus. Ver [[imagens-locais]].
