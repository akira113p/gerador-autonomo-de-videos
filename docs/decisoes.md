# Decisões do canal

## 2026-10-11 · Vídeos 3, 4 e 5: roteiros propostos; vídeo 3 com imagens de IA na nuvem
- Decisão: três roteiros novos em `piloto/propostas/` (A: The Last of Us, B: previsões de 1900, C: um dia na Revolução Francesa), com fatos checados em `pesquisa/checagem-3-roteiros-propostos.md`. O vídeo 3 (The Last of Us) vira `piloto/v3-last-of-us/`. Os vídeos 4 e 5 têm só a pasta e o roteiro; ainda não foram gerados.
- Fluxo testado no vídeo 3: **imagens no ChatGPT (plano Go) pelo navegador**, voz local (Qwen3-TTS, voz narrador-leve), jazz do 741Hz em trecho diferente do vídeo 2 (`preparar_jazz.py`, começa na faixa 3), montagem local (`montar.py`) e envio **privado** ao YouTube.
- Aprendizados (para não repetir): (1) o ChatGPT Go tem **limite diário de imagens (~150 por dia)**, depois "redefinido em 22 horas"; (2) a imagem de referência anexada (`referencia_estilo.jpg`, feita de cenas do vídeo 2) segura bem o estilo, mas cenas com palavras como "gritty" saem escuras e realistas; (3) o Chrome só deixa baixar vários arquivos de um site com **"Downloads automáticos" liberado** (`chrome://settings/content/automaticDownloads`); (4) aba em segundo plano roda lenta; o Gemini nem termina de renderizar a imagem se a janela do Chrome está coberta; (5) o Gemini recusa imagem anexada como referência ("não consigo editar imagens ainda"), então só serve com a descrição do estilo em texto.
- Plano de contingência (pedido do usuário): ChatGPT, depois Gemini, depois outra conta, depois as imagens locais (Z-Image, `gerar_local.py`).
- Motivo: pedido do usuário para testar outro fluxo de imagens.
- Substitui: o fluxo só local do vídeo 2 (ComfyUI), para o vídeo 3.

## 2026-10-10 · Nome do canal: Pocket History
- Decisão: o canal se chama **Pocket History**. Identidade visual: o personagem romano com coroa de louros espiando de dentro de um bolso mostarda, fundo turquesa, título em amarelo Impact com contorno preto. Arquivos em `identidade/pocket-history/` (perfil_1/3, banner_1/3).
- Motivo: escolha do usuário entre 10 sugestões ("o nome vai ser Pocket History"). Disponibilidade do nome, do @handle e do domínio ainda não conferida.
- Substitui: nome do canal pendente.

## 2026-10-10 · Edição: música que muda ao longo do vídeo e imagem sem zoom
- Decisão: a trilha tem que ser dinâmica e leve e mudar ao longo do vídeo (não um loop único). As imagens ficam paradas, sem zoom in/out (sai o zoompan do `montar.py` do piloto).
- Motivo: pedido do usuário para o primeiro vídeo de 20 min: "musicas mais dinamicas e leves, q mudam com o longo do video, e sem ficar dando zoom in e zoom out".
- Substitui: zoom lento alternado e música única de lira do piloto v1.

## 2026-10-10 · Música do vídeo 2: jazz leve do mix "No Copyright Royalty Free 12 hours JAZZ" (741Hz)
- Decisão: trocar as trilhas do ACE-Step pelas músicas de https://www.youtube.com/watch?v=HqPsROn8e8k. "Dinâmico e leve" = esse tipo de jazz. O mix de 12 h é a mesma sequência de ~1000 s (6 faixas) repetida; o vídeo usa a sequência contínua, nivelada por faixa. Versão em `video_v2_jazz.mp4`; a versão ACE-Step (`video_v2.mp4`) fica guardada.
- Motivo: pedido do usuário ("recorte as musicas desse video e substitua").
- Risco registrado: o canal 741Hz não informa artista, faixa nem licença; "No Copyright" no título não é licença. Pode gerar reivindicação do Content ID (perda de monetização). Subir como "não listado" e conferir o Studio antes de tornar público.
- Substitui: música ACE-Step do vídeo 2 (para esta versão). Contraria a regra "música só biblioteca livre ou local" do CLAUDE.md.

## 2026-10-10 · Vídeo 2: "What Did Ancient Romans Actually Do All Day?"
- Decisão: o primeiro vídeo longo é um dia em Roma (c. 90 d.C.) hora a hora, com o poema 4.8 de Martial como espinha. Roteiro em `piloto/v2-dia-em-roma/roteiro.md`, checado em fonte primária (`pesquisa/roteiro-dia-em-roma-checagem.md`). Música gerada localmente com ACE-Step 1.5 turbo (uma trilha por bloco de capítulos).
- Motivo: "pode começar a gerar" (aprovação do tema e do roteiro).
- Substitui: —

## 2026-10-10 · Primeiro vídeo longo: ~20 min
- Decisão: o primeiro vídeo completo do canal tem ~20 min, com tema e roteiro aprovados pelo usuário antes da geração, e thumbnail feita junto.
- Motivo: pedido do usuário.
- Substitui: piloto de ~5 min (para este vídeo).

## 2026-10-09 · Voz do canal: L6_sereno_leve
- Decisão: a voz do canal é a **L6_sereno_leve** (Qwen3-TTS VoiceDesign, usada em produção por clone do modelo Base). Referência em `identidade/narrador-leve/` (`narrador_ref.wav`, `narrador_ref.txt`, `narrador.json` com a descrição completa). O britânico grave e o professor idoso continuam salvos como alternativas. As 5 variações de carisma (V1 a V5) ficam só como teste, em `C:/ai-local/piloto/vozes-qwen/variacoes-l6/`.
- Motivo: "eu queria uma voz mais leve, mas que não parecesse IA" e "a última foi a mais humana". Sobre as variações: "vamos manter a L6_sereno_leve".
- Substitui: o papel de voz principal do britânico grave (decisão de 2026-10-09 acima).
- Ressalva: a naturalidade foi avaliada em amostras de ~15 s do modo design. Ainda não foi testada no clone em trecho longo.

## 2026-10-09 · Narrador: britânico grave (Qwen3-TTS)
- Decisão: o canal tem duas vozes salvas, criadas com Qwen3-TTS VoiceDesign e usadas em produção por clone (modelo Base): "britânico grave" (`identidade/narrador/`, principal) e "professor idoso" (`identidade/narrador-professor/`). Papel de cada uma no vídeo: pendente.
- Motivo: escolha do usuário entre 6 perfis gerados ("mantenha a voz do britânico grave", "coloque o professor idoso também").
- Substitui: Kokoro como voz principal.

## 2026-10-09 · Voz: testar Qwen3-TTS, F5-TTS e Fish Speech fora
- Decisão: gerar narradores com Qwen3-TTS 1.7B (VoiceDesign + clone, Apache 2.0). F5-TTS (CC-BY-NC 4.0) e Fish Speech (CC-BY-NC-SA 4.0) ficam fora porque a licença proíbe uso comercial.
- Motivo: o usuário achou robóticas as vozes do Kokoro e do Chatterbox. O estilo de referência é o stickman explainer (pesquisa/identidade-visual-referencias.md), não os estilos de pintura testados.
- Substitui: Kokoro como voz principal (continua instalado como alternativa).

## 2026-10-08 · Stack de IA local e nicho do piloto
- Decisão: piloto no nicho **vida cotidiana histórica**. Stack base local e grátis: Z-Image (imagem), Kokoro e Chatterbox (voz), Whisper (transcrição e legendas). Visual mistura acervo real de domínio público com imagem de IA. Talvez dublar com a própria voz no futuro (só ideia).
- Motivo: "estou construindo a identidade pra ter uma base pra IA". O piloto define o estilo que a IA vai seguir.
- Substitui: —

## 2026-10-08 · Tempo: 2 h por semana, em média
- Decisão: o usuário trabalha ~2 h por semana, em média, e sempre assiste aos vídeos antes de publicar.
- Motivo: resposta à Q3b.
- Substitui: —

## 2026-10-08 · Piloto de 5 min para identidade visual
- Decisão: antes da produção em série, fazer um piloto de ~5 min que sirva de base para a identidade visual do canal.
- Motivo: "ter uma base de identidade visual, depois continuamos".
- Substitui: —

## 2026-10-08 · Cadência diária com episódios de ~30 min
- Decisão: publicar no mínimo 1 vídeo por dia, com episódios de ~30 min.
- Motivo: escolha do usuário. Risco registrado: cadência alta e saída em série são os sinais que a política de conteúdo inautêntico pune no canal inteiro (ver pesquisa/fase6-politica-youtube.md), e 1 vídeo de 30 min por dia não deixa tempo para a checagem de fatos em fonte primária.
- Substitui: "20–30 vídeos em ~3 meses" (CLAUDE.md) e a recomendação da Q3.

## 2026-10-08 · Orçamento zero
- Decisão: orçamento de US$ 0 por mês. Só ferramentas grátis e locais.
- Motivo: escolha do usuário.
- Substitui: recomendação da Q2 (US$ 20 para voz).

## 2026-10-08 · OpenMontage aprovado para teste isolado
- Decisão: clonar o OpenMontage fora do projeto, instalar dependências e rodar testes e `render_demo.py --list`. Nada do projeto depende dele ainda.
- Motivo: único repositório avaliado que cobre o pipeline pensado (roteiro, imagens, voz, edição), com risco baixo depois do vetting.
- Substitui: —

## 2026-10-08 · Skills aprovadas
- Decisão: usar `grill-me`, `grilling`, `research` e `handoff` (mattpocock/skills), adaptadas. Rejeitadas: codebase-memory-mcp, ArtCraft, knowledge-work-plugins, system-design-notes.
- Motivo: as rejeitadas não servem a um pipeline de vídeo pequeno ou dependem de nuvem paga.
- Substitui: —

## 2026-10-08 · Escopo e meta do canal
- Decisão: canal faceless **em inglês**, com dublagem depois em idiomas que pagam bem. Tempo disponível: ~2 h por semana. Aceita 6 a 12 meses sem retorno financeiro.
- Motivo: renda extra, como experimento com critério de parada.
- Substitui: —

## Pendentes (aguardando resposta do usuário)
- Q1: direção do nicho (recomendado: história narrativa autoral com acervo de domínio público)
- Q2: respondida (US$ 0).
- Q3: janela de avaliação. Cadência decidida (1/dia), falta o critério de parada em números.
- Q3b: "2 h em média" é por semana (como antes) ou por dia? Com 1 vídeo/dia, muda tudo.
- Q4: divisão das 2 h (recomendado: 60 min roteiro, 30 min visual/voz, 30 min publicação)
- Q5: nível de inglês para revisar roteiros
- Q6: canal e AdSense já existem?
- Depois destas: nicho específico, estilo visual, voz, formato e duração, idiomas de dublagem, identidade do narrador, critérios de parada numéricos.
