---
name: fluxo-imagens-nuvem
description: "Como gerar as imagens dos vídeos no ChatGPT/Gemini pelo navegador (limites, downloads, aba oculta) e o que o usuário quer como plano B"
metadata:
  node_type: memory
  type: project
  originSessionId: 71d47e20-4e4c-4779-8b3a-c7b1fe137280
  modified: 2026-10-12T00:12:05.281Z
---

O usuário pediu (2026-10-11) para o vídeo 3 gerar as imagens no **ChatGPT Go** pelo navegador (Claude in Chrome), voz local e edição pelo Claude; contingência: **Gemini → outra conta já logada → imagens locais (Z-Image)**. Nunca parar no meio: ele quer os vídeos prontos e enviados como **privado** no YouTube.

**Why:** teste de outro workflow; o Z-Image local leva ~70 s por imagem e o usuário queria comparar.

**How to apply:**
- ChatGPT Go barra em ~150 imagens por dia ("limite redefinido em 22 horas"). Anexar `piloto/v3-last-of-us/referencia_estilo.jpg` no 1º prompt de cada chat segura o estilo; palavras como "gritty/dark" fazem a cena sair realista.
- Baixar várias imagens exige liberar "Downloads automáticos" para o site no Chrome; sem isso só o 1º download passa. Para o ChatGPT, o `fetch(img.src)` do blob + `<a download>` funciona; para o Gemini, desenhar a `<img>` num canvas e usar `toBlob`.
- A página não consegue falar com localhost (Chrome bloqueia), então não dá para postar as imagens para um servidor local.
- Só a aba visível roda rápido. Com a janela do Chrome coberta (VS Code na frente), o Gemini não termina de renderizar. Laços JS devem ser guiados por MutationObserver, não só por setTimeout.
- O Gemini recusa imagem anexada ("não consigo editar imagens"); use só a descrição do estilo em texto.
- Fechar a primeira aba do grupo reinicia o grupo e as outras abas ficam fora do controle da ferramenta.

Ver `docs/decisoes.md` no projeto para o resto das decisões do canal.
