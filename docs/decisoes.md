# Decisões do canal

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
