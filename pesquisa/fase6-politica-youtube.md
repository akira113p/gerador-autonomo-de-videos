# Fase 6: política do YouTube e riscos (pesquisa de 2026-10-08)

Fontes oficiais lidas diretamente; secundárias marcadas como tal.

## 1. Conteúdo inautêntico (monetização)
Fonte: [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en)

- Atualização de 15 jul. 2025: "repetitious content" passou a se chamar "inauthentic content" e passou a incluir conteúdo "repetitive or mass-produced".
- **Não monetizável** (exemplos oficiais):
  - "Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value"
  - "AI-generated content made with generic or unoriginal templates giving the impression of mass production"
- **Monetizável** (exemplos oficiais):
  - mesma intro e outro, desde que o grosso do conteúdo varie
  - usar IA para editar roteiro ou gerar visual, se o resultado mostrar visão criativa própria
- A página não menciona voz sintética.
- Penalidade: a monetização pode ser removida **do canal inteiro**, não só de um vídeo.

## 2. Divulgação de conteúdo sintético
Fonte: [Disclosing use of altered or synthetic content](https://support.google.com/youtube/answer/14328491?hl=en)

- **Precisa divulgar:** conteúdo fotorrealista gerado ou alterado por IA. Exemplos: pessoa real dizendo ou fazendo o que não fez, filmagem alterada de evento ou lugar real, música de IA como foco do vídeo.
- **Não precisa:** conteúdo claramente não realista ou animado, roteiro, títulos, thumbnails e legendas feitos com IA, ajustes estéticos.
- Divulgar **não afeta** monetização nem alcance (texto oficial). Não divulgar de forma recorrente pode levar a remoção ou suspensão do YPP.

## 3. Requisitos do YPP
Fonte: [YouTube Partner Program overview & eligibility](https://support.google.com/youtube/answer/72851?hl=en)

- 1.000 inscritos + 4.000 horas de exibição válidas em 12 meses, **ou** 1.000 inscritos + 10 milhões de views de Shorts em 90 dias.
- Horas assistidas no feed de Shorts não contam para as 4.000 horas.
- Passa por revisão humana de política. Atingir os números não garante aprovação.
- Termos novos a partir de 1º fev. 2027, com aceite até 31 jan. 2027.

## 4. Fiscalização em 2026 (secundário, não verificado)
- Blogs relatam fiscalização ampla em 2026, incluindo encerramento de canais grandes de IA em janeiro. Os números vêm de uma única fonte secundária ([AIR Media-Tech](https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline), [aituber.app](https://aituber.app/blog/faceless-youtube-channels-demonetized-2026/)). Várias dessas fontes vendem ferramentas, então há viés.
- Consenso dessas fontes: "faceless" sozinho não é gatilho. Os sinais que somam risco são cadência alta, formato idêntico entre vídeos, ausência de comentário ou opinião e edição mínima. A avaliação é do canal inteiro.

## Implicações para este projeto
1. **O formato "slideshow de imagens IA + TTS lendo texto genérico" está literalmente na lista de exemplos proibidos.** O pipeline precisa produzir narrativa autoral: tese, opinião, conexão entre fatos.
2. **Material de acervo real** (domínio público: Wikimedia, Library of Congress, National Archives, archive.org) misturado com arte gerada reduz a cara de produção em massa e não exige divulgação. O pipeline `documentary-montage` do OpenMontage já usa essas fontes.
3. **Imagem de IA fotorrealista de pessoa ou evento histórico real exige divulgação.** Opção: estilo visual claramente ilustrado ou pintado, que não exige divulgação e cria identidade visual.
4. **Variar a estrutura dos vídeos.** Não usar o mesmo template rígido em todos.
5. **Cadência baixa (1 vídeo por semana) não é risco, é vantagem frente à política.** O problema é alcance, não monetização.
6. **Voz sintética não é proibida**, mas voz genérica (Piper ou TTS padrão) somada aos outros sinais aumenta o risco e derruba a retenção.
