# Vídeo 6: What Would YOUR Life Be Like as a Medieval Peasant?

Concluído em 2026-10-13. Enviado como **privado** ao YouTube: https://studio.youtube.com/video/Kmr76mYIkMU/edit
Título publicado: "What Would YOUR Life Be Like as a Medieval Peasant? (England, 1300)".

## Números
- 15:29 (928,6 s), 1920x1080, 30 fps, AAC, -16,5 LUFS. 182 cenas, 2.322 palavras. Narração pura: 13:30.
- 12 capítulos (ver `descricao.md`). Legenda em inglês enviada junto. Miniatura: `thumb/thumb_3.jpg` ("3 DAYS UNPAID?!").
- Personagem: Hugh, camponês de Alwalton (Hundred Rolls, 1279; 1 virgate de 25 acres, 3 dias/semana de trabalho para o abade de Peterborough). A esposa e os filhos são ficção; a descrição do YouTube avisa.

## Como foi feito
Mesmo fluxo do v8: roteiro e checagem (`pesquisa/checagem-v6-camponesa-medieval.md`, F1 a F34) por um subagente; imagens Z-Image (182, ~3 h); 14 refeitas; voz Qwen3-TTS (13,5 min); trilhas ACE-Step em 10 blocos sem buracos; `montar.py`; `gerar_thumb.py`; `gerar_descricao.py`; upload privado.

## Lições
- **Moeda saiu com símbolo de dólar** (4 cartões) e **dinheiro/estrada modernos**: estrada de asfalto com faixa tracejada ("road") e cozinha moderna com coifa. Descrever "round silver coin with a plain cross", "narrow dirt footpath", "stone-walled room with an open hearth fire".
- **Texto em cartão** erra quando é longo ou repetido: saíram "HONS", "FFORM", "CHIREH", "FAISED" e um cartão com letras embaralhadas. Resolveu usar uma ou duas palavras comuns ("DUES", "PAYMENT", "TAX", "FAILED") e o número separado.
- "Inspector" virou policial de boné verde. Descrever a roupa de época.
- Celeiro vermelho americano e macacão aparecem em algumas cenas de campo (100, 125); deixei. A 136 manteve um chapéu de cozinheiro moderno.
- Voz: "tallage" escrito "tal ij" fez o modelo soletrar; "tallidge" funcionou.

## O que ainda precisa de você
- No Studio: responder "Conteúdo alterado ou sintético" e publicar.
- Conferir os pontos de fato frágeis (detalhes na checagem):
  1. Dias de trabalho por ano (F22): "pelo menos ~250" (Clark 2018) e "~300 antes da Peste" (Allen e Weisdorf), lidos só via EconoFact.
  2. Expectativa de vida de 31 anos (F23, cena 147), de uma tabela de famílias proprietárias.
  3. "Mais da metade do gado" (F25, cena 164), um estudo só (Slavin 2012), já com "by one estimate".
  4. Rolos de Morden (F15) são de 1399 a 1406, depois da Peste; o vídeo se passa em 1300.
  5. Saltério Luttrell (F28, cena 46): confirmar nas folhas da British Library ou generalizar.
  6. Dízimo, Michaelmas e Lady Day vieram da Wikipedia (Britannica deu 403).
- Ouvir "virgate" (sai "vur git"), "Alwalton" (sai "All Walton") e "villeins".
