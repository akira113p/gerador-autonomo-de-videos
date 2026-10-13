# Publicação do vídeo 2 (Pocket History)

Os campos ficam em `publicacao.json`, que o `ferramentas/youtube_upload.py` lê. Esta lista cobre o que só se faz no YouTube Studio.

## Antes de publicar
1. Subir como **privado** ou **não listado**, com o script ou à mão. Arquivo: `video_v2_jazz.mp4` (19:22, com tela final).
2. Esperar 1 ou 2 horas e abrir **Studio → Conteúdo → coluna Restrições**. Se aparecer "Reivindicação de direitos autorais" (a música do 741Hz), decidir: aceitar, contestar ou trocar pela versão ACE-Step (`video_v2.mp4`, que não tem a tela final; para colocar, rodar o `montar.py` sem `TRILHA`).

## Detalhes (aba Detalhes)
- **Título:** What Did Ancient Romans Actually Do All Day? (Hour by Hour)
- **Descrição:** colar `descricao_jazz.md`, que tem gancho, capítulos, fontes, crédito da música e hashtags.
- **Miniatura:** use **Testar e comparar** com `thumb_3`, `thumb_2` e `thumb_4`. O YouTube mostra cada uma a uma parte do público e fica com a que der mais tempo de exibição. Se a opção não aparecer para o canal, use `thumb_3`.
- **Playlist:** criar "A Day in History", para a série de vídeos "um dia em..." (Atenas, Egito, Idade Média).
- **Público:** "Não, não é conteúdo para crianças".
- **Conteúdo alterado ou sintético:** "Não". A política pede a declaração para conteúdo realista (pessoa real dizendo o que não disse, evento real alterado, cena realista). Aqui são desenhos de bonecos e uma voz que não imita ninguém, e a descrição já informa o uso de IA. Esta é a minha leitura da regra atual; confira o texto no Studio na hora de responder.
- **Tags:** já estão no `publicacao.json`.
- **Idioma do vídeo:** inglês. **Categoria:** Educação. **Licença:** padrão do YouTube.
- **Legendas:** subir `legendas_en_jazz.srt` como "English". Ela é feita do roteiro, então é mais precisa que a automática.
- **Comentários:** ativados, ordenados por "Principais".

## Elementos finais (aba Elementos de vídeo → Tela final)
A tela final começa em **19:07** e dura 15 s.
- **Inscrever-se:** sobre o círculo, no centro.
- **Vídeo, opção "Melhor para o espectador":** sobre o retângulo "WATCH NEXT". Com o segundo vídeo publicado, troque por "Vídeo mais recente".

## Depois de publicar
- **Comentário fixado:** está no `publicacao.json`, campo `comentario_fixado`. Publique e fixe.
- **Horário:** sábado ou domingo, 10h às 12h de Brasília, ou dia de semana entre 15h e 17h (regra geral; ajuste pelo Analytics depois de ~10 vídeos).
- **Monetização:** o Programa de Parcerias exige 1.000 inscritos e 4.000 horas de exibição em 12 meses. Até lá não há anúncios, e uma reivindicação de direitos sobre a música só pesa quando o canal for monetizado ou se o dono bloquear o vídeo.

## Shorts (para trazer público para o vídeo longo)
Três trechos que funcionam sozinhos, com minutagem no `video_v2_jazz.mp4`:
| Trecho | Início-fim | Duração |
|---|---|---|
| O imposto sobre urina de Vespasiano | 8:19-8:56 | 37 s |
| Os grafites de Pompeia | 10:45-11:45 | 60 s |
| O barulho das termas (carta de Sêneca) | 12:57-13:47 | 50 s |

Precisam ser refeitos na vertical (9:16) e ter no máximo 3 min. No Short, fixe um link para o vídeo completo ("Vídeo relacionado").
