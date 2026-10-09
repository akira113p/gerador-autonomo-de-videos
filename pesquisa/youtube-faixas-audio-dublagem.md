# YouTube: faixas de áudio em vários idiomas e dublagem automática

Data da pesquisa: 2026-10-08. Fontes: apenas support.google.com/youtube e blog.youtube.

## Resumo
1. Faixa de áudio própria ("multi-language audio") é enviada só pelo YouTube Studio no desktop, em Idiomas > Adicionar idioma > Dublagem; o arquivo precisa ser áudio puro, de duração aproximada à do vídeo. Formatos exatos e número máximo de faixas não estão na página oficial.
2. A página atual diz que o recurso é para canais com acesso a recursos avançados; o blog (set/2025) fala em expansão para "milhões de criadores". Ver [disputado] na seção 1.
3. Dublagem automática: aberta a todos desde fev/2026, 27 idiomas, ativada por padrão para canais elegíveis, vídeos até 120 min. Dubs automáticos não são editáveis; só dá para revisar transcrição, publicar, despublicar, apagar. Revisão antes de publicar é opt-in.
4. Dublagem não aparece na política de monetização (página 1311392); a política "inauthentic content" trata de conteúdo em massa/repetitivo/template, e nada lido liga dublagem a ela.
5. Divulgação de conteúdo sintético: a página 14328491 lista "clonar a própria voz para dublagens" como edição menor, sem divulgação. Dublagem de terceiros ou fazer alguém "dizer" algo que não disse cai na regra geral. Divulgar não afeta audiência nem monetização.

Legenda: [verificado] = li a página oficial e ela diz isso; [disputado] = páginas oficiais divergem ou há ressalva; [não verificado] = não consegui confirmar nas páginas oficiais.

Nota de método: o WebFetch resume a página com um modelo menor, então as citações abaixo vêm de resumos/extrações dessas ferramentas, não de leitura integral do HTML. Algumas páginas vieram truncadas (marcado onde aplicável).

## 1. Faixa de áudio própria (multi-language audio)

Fonte principal: https://support.google.com/youtube/answer/13338784?hl=en (título atual "Add Multi-language features to your videos"; título antigo "Add multi-language audio tracks to your videos").

- Permite adicionar faixas de áudio extras a um vídeo ou Short. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Upload em vídeos novos ou existentes, no YouTube Studio no desktop; a página não traz passos para mobile. [verificado quanto ao desktop; mobile = não verificado (a página não cobre)] https://support.google.com/youtube/answer/13338784?hl=en
- Passos: Studio > Idiomas > selecionar o vídeo > Adicionar idioma > ao lado de "Dublagem" clicar Adicionar > escolher o arquivo > Publicar. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Requisito do arquivo: "Files must be in a supported audio-only file format and roughly the same length as your video." [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Formatos específicos aceitos: a página não lista. [não verificado]
- Número máximo de faixas por vídeo: a página não informa. [não verificado] O blog cita Mark Rober com média de "mais de 30 idiomas por vídeo", o que mostra que há muitas faixas, mas não é um limite declarado. https://blog.youtube/news-and-events/multi-language-audio/
- Quem tem acesso [disputado]: a página (fetch de 2026-10-08) diz "currently available to creators with access to Advanced features"; uma outra versão da mesma página, vista nos resultados de busca, fala em "subset of creators ... expanding access gradually". O blog de 10/set/2025 anuncia "expansão para milhões de criadores nas próximas semanas" sem critérios. https://support.google.com/youtube/answer/13338784?hl=en e https://blog.youtube/news-and-events/multi-language-audio/
- Recursos avançados: exigem telefone verificado e, depois, histórico suficiente do canal ou verificação por ID/vídeo; a tabela de recursos lista "Multi-language features" no nível avançado. [verificado] https://support.google.com/youtube/answer/9890437?hl=en e https://support.google.com/youtube/answer/9891124?hl=en&co=GENIE.Platform%3DDesktop
- A funcionalidade não gera dublagem; é preciso gravar ou contratar. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Se já existe dub automático no idioma, é preciso apagá-lo antes de subir o seu. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Direitos autorais: se o conteúdo protegido na faixa secundária for diferente do áudio original, o arquivo pode ser removido. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Substituir faixa: Idiomas > vídeo > Excluir ao lado de "Áudio" no idioma > subir nova. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Cortes/trocas no áudio original do vídeo se propagam para as faixas secundárias. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Legendas automáticas ficam disponíveis no idioma do áudio original; analytics permite ver visualizações/tempo de exibição por idioma de áudio. [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Miniaturas localizadas (vídeos longos) estão na mesma página; em set/2025 estavam em piloto com poucos criadores segundo o blog. [verificado] https://support.google.com/youtube/answer/13338784?hl=en e https://blog.youtube/news-and-events/multi-language-audio/
- Resultados reportados pelo YouTube: mais de 25% do tempo de exibição em idioma não primário (dado de julho/2025). [verificado como alegação do YouTube] https://blog.youtube/news-and-events/multi-language-audio/

## 2. Dublagem automática do YouTube

Fontes: https://support.google.com/youtube/answer/15569972?hl=en (Use automatic dubbing, versões Computer e Android) e https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/ (4/fev/2026).

- Disponibilidade: "open to everyone", 27 idiomas suportados, segundo o blog de 4/fev/2026. [verificado] https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Ativada por padrão para criadores elegíveis; quem não tem pode usar acesso antecipado em Configurações avançadas > Ativar. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Onde ligar/desligar: desktop = Studio > Configurações > Canal > Configurações avançadas > "Allow automatic dubbing"; app Studio (Android) = Configurações > Conteúdo > Automatic dubbing. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Os dubs são gerados no upload e publicados conforme a sua configuração; podem ser gerados também para vídeos antigos. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Revisão: marcar "Manually review dubs before publishing" (desktop) ou "Publish manually" (app). Prévia, revisão de transcrição, publicar, despublicar e apagar só no Studio no computador. Dubs despublicados podem ser republicados; apagados não voltam. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Editar: "You cannot edit automatic dubs." A revisão da transcrição é só leitura. Para corrigir tradução errada, ajustar o idioma original do vídeo/canal, o que regenera os dubs. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Inelegíveis: vídeos com mais de 120 minutos; pouca ou nenhuma fala; idioma original não suportado ou não detectado; fala rápida demais; conteúdo com copyright/reivindicação de copyright (a versão Android diz "copyright claims", a desktop diz "copyrighted content"). [verificado, com leve diferença de redação] https://support.google.com/youtube/answer/15569972?hl=en
- Filtro por vídeo: o blog diz que filtros novos reconhecem quando um vídeo não deve ser dublado (música, vlog sem fala). [verificado] https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Idiomas (tabela da página, versão Android lida): original > dubs disponíveis; * = fala expressiva. [verificado; a página diz que a lista cresce, e o Studio mostra por vídeo, inclusive opções "experimentais"]
  - English > Arabic, Bengali, Dutch, French*, German*, Hebrew, Hindi*, Indonesian*, Italian*, Japanese, Korean, Malayalam, Polish, Portuguese*, Punjabi, Russian, Spanish*, Tamil, Telugu, Ukrainian
  - Arabic, Bengali, Chinese, Chinese (Traditional), Dutch, Farsi, French, German, Hebrew, Indonesian, Italian, Japanese, Malayalam, Polish, Punjabi, Romanian, Russian, Swahili, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese > English (com * em Arabic, Bengali, French, German, Indonesian, Italian, Russian, Telugu, Ukrainian)
  - Hindi > Bengali, English*; Korean > English* ou Indonesian; Portuguese > English*, Spanish; Spanish > Arabic, English*, Portuguese
  - Fonte: https://support.google.com/youtube/answer/15569972?hl=en
- Contagem de idiomas [disputado]: o blog diz 27; a tabela que li tem mais pares e um conjunto de idiomas de origem diferente do que "27" sugere à primeira vista (não reconciliei a contagem). Uma versão da página vista via busca descrevia as listas por direção (para inglês / a partir do inglês), mais antiga. https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/ e https://support.google.com/youtube/answer/15569972?hl=en
- Fala expressiva: disponível em todos os canais em 8 idiomas (inglês, francês, alemão, hindi, indonésio, italiano, português, espanhol); a página diz que nem sempre é aplicada. [verificado] https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Lip sync: experimental, só canais selecionados; altera os movimentos labiais do falante; ativar em "Allow experimental lip sync" (desktop). [verificado] https://support.google.com/youtube/answer/15569972?hl=en e https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Qualidade: varia por idioma; erros de pronúncia, sotaque, ruído; nomes próprios, expressões e jargão são mais difíceis; correspondência de voz imperfeita. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Rótulo ao espectador: vídeos com esses áudios são marcados como "auto-dubbed" na descrição. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- Alcance: o blog afirma "no negative impact on your original video's discovery algorithm". [verificado como alegação do YouTube] https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Limite de número de dubs por vídeo, Shorts e lives: a página não trata. [não verificado]

## 3. Títulos e descrições traduzidos

Fonte: https://support.google.com/youtube/answer/6289575?hl=en

- Passos (Studio desktop): Legendas (Subtitles) > vídeo > Adicionar idioma > em "Título e descrição" clicar Adicionar > preencher > Publicar. Se o vídeo não tem idioma original definido, o Studio pede para escolher e confirmar. [verificado]
- Upload em massa de CSV via Content Manager (a página escreve ".cvs") para quem usa conteúdo reivindicado. [verificado] https://support.google.com/youtube/answer/6289575?hl=en
- Limites de caracteres e diferenças mobile/desktop: a página não informa. [não verificado]
- Títulos/descrições traduzidos podem ser buscados pelos espectadores nos idiomas preferidos. [verificado] https://support.google.com/youtube/answer/13339776?hl=en
- A página de dublagem automática diz que os espectadores podem definir idiomas preferidos para áudio, título e descrição. [verificado] https://support.google.com/youtube/answer/15569972?hl=en
- O blog de multi-language audio (set/2025) não menciona títulos/descrições traduzidos. [verificado como ausência] https://blog.youtube/news-and-events/multi-language-audio/

## 4. Efeito sobre monetização / YPP

Fonte: https://support.google.com/youtube/answer/1311392?hl=en (página truncada no fetch; li só o que veio).

- A política YPP "inauthentic content" (antes "repetitious content") foi renomeada em 15/jul/2025, descrita como atualização menor. O termo aparece só no log de atualizações. [verificado] https://support.google.com/youtube/answer/1311392?hl=en
- Texto de política relevante: conteúdo "que parece feito com template", canais com vídeos "intercambiáveis" não monetizam; conteúdo gerado por IA com "templates genéricos ou não originais dando impressão de produção em massa" não é permitido; é aceitável usar IA para editar roteiros ou gerar fundos se a "visão criativa" for demonstrada. [verificado] https://support.google.com/youtube/answer/1311392?hl=en
- Conteúdo reutilizado: não monetiza quem pega conteúdo alheio com mudanças mínimas, "mesmo com permissão do criador original"; o teste é haver diferença significativa entre original e o seu vídeo. [verificado] https://support.google.com/youtube/answer/1311392?hl=en
- A página, nas partes que li, não menciona dublagem nem tradução ("dub" não encontrado; "translat" só em link de navegação). Portanto não há regra explícita de que dublar ou traduzir afeta a monetização. [verificado como ausência nas partes lidas; resto da página truncado = não verificado]
- Interpretação (minha, não está escrita no YouTube): dublar o seu próprio vídeo original não deveria cair em "reutilizado", mas dublar/traduzir vídeo de terceiros com pouca alteração pode cair na política de conteúdo reutilizado, e canais com saída de template em massa podem cair na política de inauthentic. [não verificado, inferência]
- Divulgação de IA "won't limit a video's audience or impact its eligibility to earn money". [verificado] https://support.google.com/youtube/answer/14328491?hl=en

## 5. Dublagem sintética e divulgação de conteúdo alterado/sintético

Fonte: https://support.google.com/youtube/answer/14328491?hl=en

- Exige divulgação: conteúdo realista que faz uma pessoa real parecer dizer/fazer algo que não fez; altera filmagem de evento/lugar real; gera cena realista que não ocorreu; música gerada por IA como foco do vídeo. Exemplo: "Making it appear as if someone gave advice that they did not actually give". [verificado]
- Não exige divulgação (lista de edições menores): "Cloning one's own voice to create voice overs or dubs", "Caption creation", "Video sharpening, upscaling or repair and voice or audio repair", "Using effects to enhance previously recorded audio", "Production assistance ... script, thumbnail, title". [verificado]
- A página não cita explicitamente "tradução" nem "dublagem automática do YouTube". [verificado como ausência]
- Dub automático do YouTube: a página de dublagem automática lida não traz exigência de divulgação além do rótulo "auto-dubbed" na descrição, aplicado pelo YouTube. [verificado como ausência nas páginas lidas]
- Inferência: dub com voz clonada de outra pessoa real, ou que a faça "dizer" o que não disse, se enquadra na regra de divulgação; a própria voz não. Não há linha oficial sobre voz sintética genérica (TTS) narrando seu próprio roteiro. [não verificado]
- Rótulos: "Yes" no Studio gera rótulo (no player para fotorrealista, na descrição expandida para animado). O YouTube pode aplicar rótulo automaticamente (ferramentas de IA próprias, metadados C2PA, detecção). Quem repetidamente não divulga pode receber rótulo manual ou penalidades, inclusive remoção ou suspensão do YPP. [verificado] https://support.google.com/youtube/answer/14328491?hl=en
- Divulgação não limita audiência nem afeta elegibilidade de monetização. [verificado] https://support.google.com/youtube/answer/14328491?hl=en

## 6. Como o espectador escolhe o idioma

- Padrão: faixas usam o idioma preferido do espectador, "determined by their watch history". [verificado] https://support.google.com/youtube/answer/13338784?hl=en
- Preferência explícita: blog de fev/2026 descreve configuração "Preferred Language", em vez de depender só do histórico. [verificado] https://blog.youtube/news-and-events/youtube-auto-dubbing-expressive-speech/
- Android: foto de perfil > Configurações > Idiomas > Preferred languages (vale para áudio, títulos e descrições). Conteúdo já em um dos idiomas preferidos mantém o áudio original. Por vídeo: player > Configurações > Faixa de áudio > escolher idioma. [verificado] https://support.google.com/youtube/answer/13339776?hl=en
- Passos para computador/iOS: a extração dessa página trouxe só o Android. [não verificado]
- Espectador pode alternar entre original e dublado por vídeo. [verificado] https://support.google.com/youtube/answer/15569972?hl=en

## 7. Limitações e observações
- Dublagem própria é só desktop Studio; dub automático só pode ser revisado/publicado/apagado no desktop.
- Dubs automáticos não são editáveis, só publicar/despublicar/apagar (apagados não voltam).
- Vídeos acima de 120 min, com pouca fala, com copyright ou em idioma não suportado não recebem dub automático.
- Se você sobe dub próprio para um idioma que já tem dub automático, precisa apagar o automático antes.
- Legendas automáticas ficam só no idioma do áudio original.

## Não consegui confirmar
- Lista oficial de formatos de arquivo aceitos para a faixa própria (a única lista que apareceu, em https://support.google.com/youtube/answer/4603579, é para parceiros de conteúdo/música e não li essa página).
- Número máximo de faixas de áudio por vídeo.
- Critério exato e atual de acesso ao multi-language audio ("recursos avançados" vs "subconjunto de criadores"); se "Multi-language features" no nível avançado inclui exatamente isso.
- Passos de multi-language audio no mobile (a página só descreve desktop) e passos de preferência de idioma em computador/iOS.
- Contagem exata e lista consolidada dos "27 idiomas" do blog versus a tabela do Help; a tabela pode ter sido alterada desde o fetch.
- Limites de caracteres para títulos/descrições traduzidos.
- Se dublagem (própria ou automática) tem qualquer tratamento específico na política YPP: a página 1311392 foi lida só parcialmente (truncada).
- Se dublagem de vídeo de terceiros é tratada como "reutilizado" ou "inauthentic": não há texto oficial que diga.
- Se voz sintética (TTS genérica ou voz clonada de outra pessoa) em dublagem própria exige divulgação além da regra geral de "pessoa real parecer dizer algo".
- Suporte a Shorts, lives e limite de número de dubs na dublagem automática.
- Leitura integral das páginas: as ferramentas entregam resumos; recomendo conferir as URLs diretamente antes de decisões de produto.
