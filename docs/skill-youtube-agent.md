# Skill youtube-agent (Jakeschincariol/youtube-agent-skill)

- Origem: https://github.com/Jakeschincariol/youtube-agent-skill (commit a2feb21), licença MIT. Autor: Jake Schincariol.
- Instalada em 2026-10-19 em `.claude/skills/yt-*` (11 skills), licença em `.claude/skills/LICENSE-youtube-agent-skill.txt`.
- Revisão antes de instalar: seis scripts Python (535 linhas), só stdlib, só leitura de arquivo local, sem rede, sem subprocess, sem eval. Nada publica nem acessa conta: as skills escrevem, o usuário envia.
- Adaptações nossas: o caminho do perfil de voz mudou de `~/.claude/youtube/voice.md` para `.claude/youtube/voice.md` (dentro do projeto). Preenchido em `.claude/youtube/voice.md` (rascunho). O template original ficou em `.claude/youtube/voice-template.md`.
- Nota do autor: `hookscore.py` é heurística calibrada em 74 hooks curtos; separa hook ruim de hook real, mas não separa os acertos de um criador dos erros dele. No nosso canal o linter de títulos também não previu as views (ver `docs/analise-canal-2026-10-19.md`).

## Como cada skill encaixa no projeto
| Skill | Encaixe | Observação |
|---|---|---|
| `yt-package` | **Alto.** CTR de 1,0% é o gargalo. | Rodar em todo vídeo antes do upload. Limite de ~60 caracteres no título. O padrão "(parêntese com ano)" passa disso. |
| `yt-script` | **Alto, com adaptação.** | Os 21 formatos de hook e o placar servem para o início do roteiro. O `[ON SCREEN]` aqui é imagem ou cartão, não rosto. Não substitui `roteiro.md` nem a checagem de fatos (`research`). Regra "sem apresentação do canal antes do 0:45" já é nossa. |
| `yt-retention` | **Alto.** | Precisa do CSV de retenção do Studio (download manual) e aceita o `.srt`, que já geramos (`legendas_en.srt`). Diz em que frase as pessoas saem. |
| `yt-seo` | Médio. | `gerar_descricao.py` já monta descrição e tags. Usar a skill para as 3 buscas que cada vídeo deve ganhar. |
| `yt-chapters` | Baixo, como validador. | `montar.py` já gera capítulos com tempos exatos. `chapters.py` pode conferir as regras (00:00, mínimo 3, mínimo 10 s). |
| `yt-viral` | Médio. | Ranqueia vídeos de um nicho pelo múltiplo sobre a mediana do próprio canal. Útil para achar o próximo "Last of Us". Precisa coletar views de canais (yt-dlp ou lista manual), só páginas públicas. |
| `yt-shorts` | Médio. | Cortar Shorts dos vídeos longos como porta de entrada. Falta no pipeline um passo de montagem vertical. |
| `yt-plan` | Atenção. | Recomenda 3 envios por semana, não 1 por dia. Conflita com a decisão de cadência diária de 2026-10-08 e com as ~2 h por semana. Os números do canal (volume não gerou views) apoiam rever a cadência, mas a decisão é do usuário. |
| `yt-comment` | Baixo por enquanto. | O canal tem 0 comentários. Útil quando houver. |
| `yt-audit` | Médio. | Termina em uma correção só. Pode rodar de novo em 1 mês. |
| `yt-edit` | **Não se aplica.** | Corta pausas e "ahn" de gravação ao vivo. Nosso áudio é TTS e já sai cortado. |

## Ordem de uso sugerida por vídeo
1. `research` (fatos) e roteiro no formato do Last of Us.
2. `/yt-script` nos 15 primeiros segundos.
3. `/yt-package` com título e texto de miniatura juntos.
4. Produção normal (imagens, voz, `conferir.py`, `montar.py`).
5. `/yt-seo` e `/yt-chapters` (validação) antes do upload.
6. Uma semana depois: exportar retenção e rodar `/yt-retention`.
