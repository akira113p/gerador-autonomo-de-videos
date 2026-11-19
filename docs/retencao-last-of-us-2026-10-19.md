# Retenção do vídeo The Last of Us (2026-10-19)

Fonte: export "Retenção de público" do Studio, 11 a 19 out 2026. CSVs em `docs/retencao/last-of-us/` (`Todos.csv` é a curva; `Orgânicos.csv` traz a coluna "em comparação com outros vídeos"; os de anúncio, atividade e inscritos vieram vazios). Texto cruzado com `piloto/v3-last-of-us/legendas_en.srt` (1% do vídeo ≈ 9,7 s). Rodado com `yt-retention` e conferido à mão.

**Cuidado com a amostra:** ~129 espectadores (cada um vale ~0,78 ponto percentual). Os espectadores recorrentes são ~10 pessoas: ignorar. Leia como sinal.

## A curva (retenção absoluta)
| Ponto | Tempo | Ainda assistindo |
|---|---|---|
| 0% | 0:00 | 103% (reassistidos) |
| 1% | 0:10 | 70% |
| 3% | 0:29 | 54% |
| 10% | 1:37 | 46% |
| 30% | 4:50 | 37% |
| 50% | 8:04 | 32% |
| 75% | 12:05 | 26% |
| 90% | 14:30 | 22% |
| 99% | 16:00 | 14% |

Terminou com ~14% de quem entrou, bom para um vídeo de 16 min. A queda no meio é lenta (0,4 ponto por 1%): é ritmo, não conteúdo.

## O que a curva mostra
1. **A maior perda é nos primeiros 10 s: 33% do público sai** em "It's an ordinary morning at the end of September" e "You wake up, make coffee, and check the news". O título só é confirmado em 0:17 ("In the world of The Last of Us…"). Ou seja, um terço sai antes de ouvir o nome do universo que o fez clicar. Em 30 s já saíram 49%.
   - Ressalva: a coluna de comparação do Studio mostra esse começo **acima** de outros vídeos (+28 pontos em 0:10), então não é um desastre; mas é a maior perda isolada e a mais barata de consertar.
2. **Melhor trecho: 2:15 a 4:00 (+20 a +27 pontos vs outros vídeos, pico em 3:52)**: capítulos "The fungus is real" e "Day 1". São fatos reais que o espectador reconhece da própria vida: o apagão de 2003 e o papel higiênico de 2020.
3. **Queda em 4:20 a 5:00 (−7 a −15):** "supermarkets / trucks stop / count cans / store water" (semana 1). Lista de preparação, sem surpresa.
4. **A segunda metade é a fraca: a partir de ~9:50 o vídeo fica 25 a 55 pontos abaixo dos outros.** Piores pontos: 86 a 99% (~13:50 até o fim, −45 a −56) = "Who still knows how to make penicillin", comparação com o Império Romano, "So, would you survive?" e o fechamento; e 71 a 77% (~11:30 a 12:15, −30 a −41) = remédio acabando, metrô de Nova York, Chernobyl.
5. **O pedido de comentário aos 15:37 coincide com a queda de 3% do fim.** É o fim do vídeo; não é prioridade.

## O que isso muda nos próximos vídeos (hipóteses, uma amostra só)
1. **Confirmar o título na primeira frase.** Algo como "In The Last of Us, you…" nos primeiros 5 s, sem a cena de "acordar e fazer café". É o que `yt-script` pede (confirmar o clique antes de qualquer cena).
2. **Ancorar em fatos reais que o espectador viveu** logo no começo (blackout, 2020, preços, clima). Foi o trecho mais forte.
3. **Concentrar o melhor nos primeiros ~7 min** (metade do público já saiu em 6:30 a 8:00) e **encurtar a segunda metade**, principalmente os últimos 3 min. Testar um vídeo de ~12 a 14 min em vez de 16.
4. **Evitar listas de preparação sem surpresa** no meio (a semana 1).
5. Os capítulos 2:26 e 3:46 ("Day 1", "Week 1") podem virar o formato do miolo: dias e horas concretos.

## Limite desta leitura
Só temos o Last of Us. Falta o CSV do vídeo de Roma (tema de busca, 142 views) para saber se a segunda metade também cai ali. Antes de mudar o formato, comparar os dois.
