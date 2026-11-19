# Análise do canal Pocket History (2026-10-19)

Fonte: YouTube Studio (Painel, Conteúdo, Estatísticas), janela dos últimos 28 dias (21 set a 18 out 2026).
Canal: UC6FUboTilfAi8h_ajJcDzYw. Amostra pequena: trate como sinal, não como regra.

## Números do canal
- 372 views, 15,4 h de exibição, 1 inscrito, 13,5 mil impressões, CTR 1,0%, duração média 4:56.
- 96,6% das impressões vêm de recomendação do YouTube.
- Origem das views: vídeos sugeridos 44,4%, pesquisa do YouTube 40,9%, direta/desconhecida 10,5%, playlists 1,3%.
- 0 comentários em todos os vídeos. Likes: Last of Us 4, Roma 1.

## Por vídeo
| Vídeo | Publicado | Views | Duração média assistida | Retenção aos 0:30 |
|---|---|---|---|---|
| What Would YOUR Life Be Like in The Last of Us Apocalypse? (16:07) | 12 out | **195** | 5:04 (31,5%) | 56% |
| What Did Ancient Romans Actually Do All Day? (19:23) | 10 out | **142** | 5:15 (27,2%) | 53% |
| How People in 1900 Imagined the Year 2000 (16:06) | 12 out | 17 | 2:43 (16,9%) | n/d |
| What Was Daily Life Like During the French Revolution? (17:16) | 13 out | 13 | 4:40 (27,1%) | n/d |
| What Would YOUR Life Be Like on a Viking Ship? (14:44) | 14 out | 5 | 0:13 (1,5%), CTR 2,1% | n/d |
| Oregon Trail (14:32) | privado desde 13 out | 0 | | |
| Medieval Peasant (15:29) | privado desde 13 out | 0 | | |

## O que deu certo
1. **Last of Us + Roma = 91% das views.** Foram os dois que o YouTube recomendou.
2. **O comparativo mais limpo:** Last of Us e 1900/2000 foram publicados no mesmo dia (12 out). Um teve 195 views e o outro 17. Mesma janela, mesma voz, mesmo formato de produção: a diferença é tema e embalagem, não produção.
3. **Tema com gancho de cultura pop ou de busca forte** ("Last of Us", "Ancient Romans"). Os temas abstratos (1900, Revolução Francesa) ficaram em 13 a 17 views.
4. **Miniatura com promessa direta:** "WOULD YOU SURVIVE?" e "75 MINUTES = 1 HOUR?!".
5. **A retenção de quem clica é boa para vídeo longo:** 27% a 31% de um vídeo de 16 a 19 min, e mais de 50% ainda assistindo aos 0:30. O roteiro e a voz seguram.

## O que não deu certo
- **CTR de 1,0%** é o gargalo: 13,5 mil impressões, 140 views engajadas.
- **1 inscrito e 0 comentários.** Quem assiste não volta nem fala.
- **Viking:** 0:13 de duração média com 5 views. Poucos dados, mas ver o início do vídeo e a miniatura.
- **1900/2000:** perde o público cedo (2:43 de 16:06).
- **Revolução Francesa:** retenção parecida com Roma (27%), mas quase sem impressões. O problema é chegar ao público, não o conteúdo.
- Dois vídeos prontos (Oregon Trail, Medieval Peasant) estão privados e não serão publicados (avaliação do usuário: ficaram ruins).

## Teste do linter de títulos (yt-package, rodado em 2026-10-19)
O score do linter **não previu** o resultado: 1900/2000 tem a nota mais alta (94) e teve 17 views; Last of Us tem 84 e teve 195. O próprio autor da skill avisa que o linter é heurístico. Fatos úteis dele:
- Os 3 títulos com "(parêntese com ano)" passam de 60 caracteres (74, 77 e 72) e são cortados na busca do desktop: Viking, Oregon Trail, French Revolution. Medieval tem 67.
- Last of Us e Roma estão em 58 e 59 caracteres, dentro do limite. Coincidência com o resultado, mas vale manter títulos até ~60.
- Nas miniaturas, o linter acusa repetição do título no texto ("WOULD" e "HOUR") e falta de número/nome nos dois. Não parece ter pesado.

## Decisão que sai daqui
Foco de postagem: vídeos no formato do Last of Us (ver `docs/decisoes.md`, 2026-10-19).

## Próximos passos sugeridos (não decididos)
1. Oregon Trail e Medieval Peasant (privados) **não serão publicados**: o usuário os considerou ruins. Os próximos vídeos serão novos, no formato Last of Us. Direitos de uso das franquias não limitam a escolha do tema (decisão do usuário, 2026-10-19).
2. ~~Exportar o CSV de retenção do Last of Us~~ Feito: ver `docs/retencao-last-of-us-2026-10-19.md`. Falta o de Roma (Studio, vídeo, Analytics, Engajamento, baixar "Retenção do público") para comparar.
3. Antes de cada vídeo novo, rodar `/yt-script` (hooks) e `/yt-package` (título + miniatura) sobre o roteiro. O CTR é o que mais pesa agora.
4. Testar miniatura/título novos nos vídeos que já têm impressões (Revolução Francesa, 1900).
5. Um pedido de inscrição e uma pergunta que gere comentário, sem antes do 0:45.
