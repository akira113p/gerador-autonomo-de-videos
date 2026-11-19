# Vídeo 11: What Would YOUR Life Be Like on the Oregon Trail?

Concluído em 2026-10-13. Enviado como **privado** ao YouTube: https://studio.youtube.com/video/cSkp336whPs/edit
Título publicado: "What Would YOUR Life Be Like on the Oregon Trail? (Walking 2,000 Miles, 1850)".

## Números
- 14:31 (871 s), 1920x1080, 30 fps, AAC, -16,5 LUFS. 183 cenas, 2.083 palavras. Narração pura: 12:33.
- 12 capítulos (ver `descricao.md`). Legenda em inglês enviada junto. Miniatura: `thumb/thumb_2.jpg` ("2,000 MILES ON FOOT?!").
- Espinha: você sai de Independence, Missouri, em abril de 1850, a pé. A única pessoa real seguida em detalhe é Amelia Knight (diário de 1853). Mitos desmentidos: ninguém ia sentado na carroça; o Conestoga não era usado; ataques foram raros e a cólera foi a maior causa de morte; o círculo de carroças era sobretudo curral para o gado. Tese: o perigo era um balde de água e não uma flecha, e a "terra vazia" do fim era a casa de outros povos.
- Povos indígenas: nenhuma pessoa indígena foi desenhada (só cartões, paisagens, mãos e bisões), de propósito.

## Como foi feito
Mesmo fluxo do v8 e v6: roteiro e checagem (`pesquisa/checagem-v11-oregon-trail.md`, F1 a F32) por um subagente; imagens Z-Image (183, ~3 h); 10 refeitas; voz Qwen3-TTS (12,5 min); 11 trilhas ACE-Step (a "serra" precisou de 11 tentativas para ficar sem buraco); `montar.py`; `gerar_thumb.py`; `gerar_descricao.py`; upload privado.

## Lições
- Textos de cartão errados em 5 casos: "20,00+", "300,0I0+", "FAISTER", "SAFSSSAGE", "LET'S CHECK" com "#" embaralhado. Resolveu pondo uma palavra curta por cartão e o número sozinho ("FAST/STRONG", "SAFE", "CHECK", "TOLL").
- Placa "ONE WAY" saiu como placa de rua moderna; "TOLL" funcionou. Vagões em fila saem como trenzinhos coloridos: pedir "covered wooden wagons with white canvas covers and ox teams".
- Nomes que o modelo erra na voz: "Conestoga" (saiu "Kani Stogu"), "Laramie" ("Lair Ami") e "Missouri". Grafias que funcionaram: `konnistoga`, `larremee`, `mizzoori`. Grafia com sílabas separadas por espaço ("kon ih stoh guh") quebra a fala.
- Cenas deixadas de propósito com anacronismo (gags): 027 (van de mudança), 124 (cinema), 131 (guarda-parque), 005 (posto de gasolina). Cena 110 tem veículos que parecem vans; 135 tem um carrinho dobrável. Vale olhar.

## O que ainda precisa de você
- No Studio: responder "Conteúdo alterado ou sintético" e publicar.
- Conferir os pontos de fato frágeis (detalhes na checagem):
  1. Mortes totais (cenas 11 e 117): "pelo menos 20 mil" é do BLM, mas as estimativas vão de 6 mil a 30 mil; o texto diz "estimates vary".
  2. Diário de Amelia Knight: li só por resumos. Conferir no texto integral as citações "Dreary times, wet and muddy", "Children are getting used to them" e "This is the journey's end", e a ordem dos fatos de setembro de 1853.
  3. Horse Creek (cena 150): o corte das anuidades de 50 para 10 anos vem de uma coleção da UND; conferir o texto do tratado.
  4. Unruh, Schlissel e Mattes não foram abertos; os números chegam por resenhas, NPS e museus. Donner (cena 70): 87 pessoas e 48 sobreviventes, as fontes divergem.
  5. Mais frágeis: "mulheres e crianças coletavam esterco" (cena 85); a data exata da lei de terras de 1850; o atalho de Hastings.
  6. Revisar o tom dos capítulos 8 e 9 (ataques e povos indígenas).
