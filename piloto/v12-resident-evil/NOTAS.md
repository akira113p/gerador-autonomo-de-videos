# Vídeo 12: Could YOU Escape Raccoon City? (Resident Evil 2026)

Pronto em 2026-10-20. `video_v12.mp4` (12:22, AAC, para publicar) e `video_v12_vscode.mp4` (Opus, toca no preview do VS Code). Miniatura `thumb/thumb_1.jpg` ("ONE NIGHT LEFT"), descrição `descricao.md`, legenda `legendas_en.srt`, dados de envio `publicacao.json`.

**Não foi enviado ao YouTube:** o token do `ferramentas/youtube_upload.py` expirou (`invalid_grant`). Para subir: `C:/ai-local/venv-yt/Scripts/python.exe ferramentas/youtube_upload.py --autorizar` (abre o navegador) e depois `... youtube_upload.py piloto/v12-resident-evil`.

## Como foi feito
- Roteiro: `roteiro.md` (cópia de `piloto/propostas/d-raccoon-city.md`, onde ficam as fontes). 141 cenas, 1.895 palavras.
- Imagens: 001–014 no ChatGPT (folha de personagem `imagens_gpt/p0.png` + cenas; 008, 009, 011 e 013 refeitas por texto em cirílico e cenário russo; a 009 usada é a versão "cidade em chamas"). 015–141 no FLUX.2 klein 4B local com 2 referências (`ferramentas/klein_ref.py`, prompts em `prompts_local.json`, log em `imagens_local_log.txt`), 27 cenas longas com segunda imagem `NNNb`. ~38 s por imagem, 101 min no total, ~30% refeitas.
- `compor.py`: relógio e bateria no canto (o celular morre no frio na cena 115) e 20 cartões com número, por código.
- Voz: Qwen3-TTS, voz narrador-leve, 643,8 s. `conferir.py`: 119 OK, 22 DIF só de número escrito por extenso e grafia de nome (Cregger → "Kreger" na transcrição, a fala está certa).
- Trilhas (`preparar_trilhas.py`): tensa (THRLL) na abertura, baixa; jazz ("Night on the Docks - Sax", Kevin MacLeod, CC BY 3.0) às 9:40 PM; tensa até o amanhecer; piano (Millennials Melody) no fim. Loudness final -16,7 LUFS.

## Lições
- Rodar a voz com `&` dentro do Bash deixou dois processos de TTS vivos ao mesmo tempo: 2,5 min por cena em vez de 12 s. Usar só tarefa em segundo plano da ferramenta e conferir `nvidia-smi` antes.
- No klein, a image 2 com personagem grande em primeiro plano vaza o personagem e objetos para a cena nova; usar referências de cenário.
- Imagens que destoam e ficaram: parque ensolarado no meio da noite (cena dos estudos de pânico), sino em neon, cão da raiva em estilo de ilustração médica, neve em Wuhan.

## Conferir antes de publicar
- Assistir inteiro; a cena 009 e as dos cartões.
- Fatos [D] da proposta: detalhe do soro da Umbrella (Wikipedia/MovieWeb), data do míssil (1º ou 2 de outubro, nos jogos), número de Sverdlovsk ("dozens").
