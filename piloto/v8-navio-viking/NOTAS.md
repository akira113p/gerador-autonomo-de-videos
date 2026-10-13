# Vídeo 8: What Would YOUR Life Be Like on a Viking Ship?

Concluído em 2026-10-13. Enviado como **privado** ao YouTube: https://studio.youtube.com/video/VvlEidUgXBQ/edit
Título publicado: "What Would YOUR Life Be Like on a Viking Ship? (Iceland to Greenland, 985)".

## Números
- 14:43 (883 s), 1920x1080, 30 fps, AAC, -16,2 LUFS. 178 cenas, 2.190 palavras. Narração pura: 12:47.
- Capítulos: 12 (ver `descricao.md`). Legenda em inglês: `legendas_en.srt` (enviada junto).
- Miniatura: `thumb/thumb_1.jpg` ("ONLY 14 ARRIVED", fazendeiro assustado apontando o knarr com uma vaca).

## Como foi feito (fluxo sequencial, sem subagentes na produção)
1. Roteiro e checagem: `roteiro.md` e `pesquisa/checagem-v8-navio-viking.md` (F1 a F32). Feitos por um subagente.
2. Imagens: `gerar_imagens.py` (Z-Image, ~68 s cada, 178 imagens, ~3 h). Revisão por folhas de contato: 23 imagens refeitas.
3. Voz: `gerar_voz.py` (Qwen3-TTS, narrador-leve), ~13 min para tudo. `conferir.py`: 63 DIF, quase todos número escrito em dígito ou nome próprio. Refeitas só 049, 059, 062 (Gokstad, Landnámabók, Faroes).
4. Trilha: `gerar_trilha.py` (ACE-Step, 11 blocos) e `refazer_trilhas.py` (buracos de silêncio). O bloco "nevoeiro" teve de trocar de estilo (ambiente demais) e ainda tem um trecho calmo aos 4 s.
5. `montar.py`, `gerar_thumb.py`, `gerar_descricao.py`, `publicacao.json`, `ferramentas/youtube_upload.py` (sempre privado).

## Lições para os próximos vídeos
- **Navio sai moderno** quando o prompt diz "ship", "boat" ou "harbor": apareceram navio de carga de aço, balsa, barco com cabine, leme de roda e até um galeão. O que resolveu foi usar sempre o token `{KNARR}` (descrição pela forma: casco de tábuas sobrepostas, uma vela quadrada listrada, remo de leme) e evitar "harbor", "steamship".
- "One-eyed" virou monóculo; moeda "genérica" virou símbolo de Bitcoin. Descrever o objeto pela forma ("round blank silver coin with a small cross").
- Cena 003 ainda tem maçaneta de alavanca na porta (pequeno anacronismo, não refeito). Cena 057 usa um celular de propósito (gag "no GPS").
- A cena 1 e a 2 falharam na primeira passada porque o ComfyUI ainda estava ocupado com o pedido anterior. Rodar `gerar_imagens.py` de novo gera só as que faltam.
- O 1º upload usou as credenciais já autorizadas em `ferramentas/.youtube/`.

## O que ainda precisa de você (no Studio)
- Responder "Conteúdo alterado ou sintético" (voz e imagens de IA) e publicar. O vídeo está privado.
- Comentário fixado sugerido e playlist ("What If...") estão no `publicacao.json`; o script não os aplica.
- Conferir os fatos mais frágeis antes de publicar (detalhes na checagem):
  1. 25 navios saíram e 14 chegaram: contagem mais repetida, mas uma tradução da Saga dos Groenlandeses diz 35. O texto usa "may have".
  2. Saga de Erik e Saga dos Groenlandeses divergem (queda do cavalo vs. caixa de ouro). O roteiro atribui à "saga".
  3. L'Anse aux Meadows, o artigo de 2021 (1021) e Gokstad vêm de fontes secundárias (Parks Canada e Nature não abriram). Travessia de Gokstad em 1893: 22 a 28 dias, o texto diz "about four weeks".
  4. "Probably wrapped in a wool cloak" vem de material didático.
  5. Neil Price (Children of Ash and Elm) não foi consultado.
- Ouvir a pronúncia de "knarr" (sai como "nar"), Landnámabók, Brattahlid e Gjermundbu.
