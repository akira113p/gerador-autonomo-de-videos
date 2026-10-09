# Relatório final: nichos faceless em inglês (Fases 1 a 6)

Data: 8 out 2026. Dados brutos completos (tabelas, ganchos, miniaturas): [canais-faceless-fases1-4-consolidado.md](canais-faceless-fases1-4-consolidado.md). Política: [fase6-politica-youtube.md](fase6-politica-youtube.md). Dublagem (documentação oficial): [youtube-faixas-audio-dublagem.md](youtube-faixas-audio-dublagem.md).

Rótulos: **OBSERVADO** (visto na página nesta sessão), **TERCEIROS** (estimativa de ferramenta externa, citada), **INFERÊNCIA** (minha leitura). Escalas: facilidade 1 (difícil) a 5 (fácil); risco 1 (baixo) a 5 (alto).

---

## 1. Tabela de nichos

| Nicho | Nº de canais faceless relevantes (vistos) | Canais novos (<18 meses) com sucesso? | RPM estimado (rotulado) | Facilidade IA + script (1–5) | Risco de desmonetização (1–5) | Nota geral e justificativa |
|---|---|---|---|---|---|---|
| Psicologia sombria / Maquiavel / Jung / estoicismo | 4 em EN + 2 clones em ES (OBSERVADO) | **Sim**: Mindplicit (361 mil inscritos, ~11 meses), Dark Psychology Coded (257 mil, ~14 meses) | Não achei faixa de terceiros específica. Social Blade usa faixa fixa US$0,25–4,00 por mil views, sem informação própria (TERCEIROS) | 4 | 4–5 | **7/10 demanda, 4/10 segurança.** Melhor sinal de crescimento, mas o molde é idêntico entre canais e a saída em massa é o que a política pune. |
| História para dormir (vídeos de 2 h ou mais) | 5 em EN + 3 em ES/PT + 1 em DE (OBSERVADO) | **Sim**: Sleepy History Channel (~14 meses, 54,6 mil, vídeos de 340 mil views), History Before Sleep (~16 meses, 59,5 mil) | História/true crime US$5–12 de CPM (OutlierKit, TERCEIROS, "planning estimate") | 5 | 4 | **6/10.** Demanda real e já replicada em 4 idiomas; é o formato mais próximo de "slideshow + voz", exemplo oficial de não monetizável. Clones minúsculos em volta. |
| True crime narrado (casos antigos/resolvidos) | 5 (OBSERVADO) | Parcial: Crime Narrator (~9 meses, 27 mil, média ~33 mil views/vídeo); Crime Signal House (5 semanas, pico de notícia) | US$5–12 de CPM (OutlierKit, TERCEIROS) | 3 | 4–5 | **4/10.** Pessoas reais, fotos de vítimas, fatos que precisam de checagem, reuso de entrevistas em canal grande. Sensacionalismo vira passivo. |
| História/mitologia narrada em formato longo | 1 verificado: History and Mythology (83,6 mil inscritos, 478 vídeos); outros só vistos em busca | Não verificado (data de criação não visível) | US$5–12 (OutlierKit, TERCEIROS) | 4 | 3–4 | **Cobertura mínima.** Um vídeo recente com 1,3 mi de views; não dá para concluir o nicho. |
| Horror / creepypasta narrado | 4 grandes (marcas de 2011–2020) | Não achei canal novo em EN com sinal | não verificado | 3 | 3 | **3/10 para replicar.** Mercado enorme, dominado por animação própria e marcas. |
| História animada | 2 grandes (SideQuest, Forgotten History) | Não em EN | não verificado | 1–2 | 2 | **Descartado para 2 h/semana** (animação artesanal). |
| Finanças / negócios | 0 faceless novos achados | Não achei | **US$15–45 de CPM (OutlierKit, TERCEIROS)**, o mais alto das fontes lidas | 3 | 3 | **Hipótese sem evidência.** Melhor CPM de terceiros, mas nenhum canal novo verificado. |
| Geopolítica, mistérios, mitologia (resultados gerais) | 0 | Não: top da busca é de criadores com rosto e marcas (Dhruv Rathee, Johnny Harris, Diary of a CEO) | não verificado | 3 | 2–3 | **Sem sinal faceless replicável** na busca feita. Não prova que não exista. |
| Ciência, espaço, animais, biografias, tech, lifestyle "top 10" | não pesquisado | não pesquisado | não pesquisado | — | — | **Fora da cobertura.** |

---

## 2. Tabela de canais (CSV)

Campos da Fase 2. "Frequência" = uploads em 30 dias (Social Blade, TERCEIROS, pode estar defasado). "Receita SB" = Social Blade, TERCEIROS; usa faixa fixa e não traz RPM próprio. "Voz" = "não verificado" (nenhum áudio ouvido) salvo onde o canal declara. "Estilo visual" vem de miniaturas e descrições, não de assistir aos vídeos. Os 7 últimos são da Fase 5 (outros idiomas); data de criação e frequência não visíveis.

```csv
nome,url,nicho,criado,inscritos,videos_total,uploads_30d_SB,duracao_tipica,estilo_visual,voz,idioma,receita_mensal_SB_TERCEIROS,risco_massa
Sleepy History Channel,https://www.youtube.com/@TheSleepyHistoryChannel,historia para dormir,2025-07-27,54600,129,9,2h00-2h58,pintura estilo IA + texto,nao verificado,EN,"US$473-7600",medio-alto
History Before Sleep,https://www.youtube.com/@historybeforesleep88,historia para dormir,2025-06-04,59500,603,6,2h30-4h15,ilustracao + emojis no titulo,nao verificado,EN,"US$146-2300",alto
Sleepy Time Historian,https://www.youtube.com/@SleepyTimeHistorianYT,historia para dormir,2024-02-12,174000,430,52,2h15-2h30+,pintura IA; banner com 3 pessoas; um video com rosto,"IA declarada na pagina Sobre (roteiro, narracao, imagens)",EN,"US$234-3700",medio (declara IA; tem marca e produtos)
History & Sleep,https://www.youtube.com/@HistoryAndSleep,historia para dormir,2016-12-23 (conta antiga),54800,557,15,5h50-7h53,fundo bege com velas e livro (marca),nao verificado,EN,"US$62-991",medio-alto
Henry's History for Sleep,https://www.youtube.com/@Henryhistoryforsleep,historia para dormir,2008-05-18 (conta antiga),28200,117,30,2h13-3h07,pintura IA + texto amarelo,nao verificado,EN,"US$53-855",alto
Mindplicit,https://www.youtube.com/@Mindplicit,psicologia sombria / filosofia,2025-11-06,361000,169,15,17-29 min,pintura escura estilo IA + 2 palavras,nao verificado,EN (titulos traduzidos),"US$786-13000",medio-alto
Dark Psychology Coded,https://www.youtube.com/@DarkPsychologyCoded,psicologia sombria / filosofia,2025-07-25,257000,167,0 (SB; video visto de 2026-08-10),26-42 min,faixa preta + 3 palavras + pintura renascentista,nao verificado,EN (titulos traduzidos),"US$349-5600",alto (molde identico ao Mindplicit)
The Shadow Work,https://www.youtube.com/@TheShadowWork,psicologia / Jung,2024-01-02,269000,308,35,42-46 min com capitulos,ilustracao vetorial plana propria,nao verificado,EN (titulos traduzidos),"US$1-16000",medio
Stoic Directions,https://www.youtube.com/@stoicdirections,estoicismo,2023-09-28,143000,649,13,33-52 min,busto P&B com texto amarelo,nao verificado,EN (titulos traduzidos),"US$526-8400",alto (erros de titulo; titulo republicado)
Crime Signal House,https://www.youtube.com/@CrimeSignalHouse07,true crime (caso em andamento),2026-09-03,5900,21,4 (SB defasado),30-42 min,colagem estilo noticiario com rostos reais,nao verificado,EN,"US$18-294 (SB defasado)",muito alto
Crime Narrator,https://www.youtube.com/@CrimeNarratorYT,true crime (casos antigos),2026-01-14,27000,107,7,25-37 min,foto real da vitima + etiqueta vermelha,nao verificado,EN,"US$15-242",medio
True Crime Uncut,https://www.youtube.com/@UncutTrueCrime,true crime,2025-04-10,50000,405,42,21-55 min,rostos reais; marca UNCUT KILLERS,nao verificado,EN (titulos traduzidos),"US$208-3300",muito alto (provavel reuso de entrevistas; INFERENCIA)
Unreal True Crime,https://www.youtube.com/@UnrealTrueCrime,true crime (edicao dublada),2023-02-27,148000,124,dado inconsistente,27-28 min,foto de casal + etiqueta,nao verificado,"EN + Latin Edition (dublagem)",nao utilizavel,medio
The Infographics Show - True Crime,https://www.youtube.com/@TheInfographicsShow-TrueCrime,true crime (animacao),2025-10-16,63000,51,10,28 min a 2h,animacao cartunesca propria,nao verificado,EN (titulos traduzidos),"US$513-8200",baixo (marca grande; nao replicavel)
EL MAGE DEL ESTOICO,https://www.youtube.com/@elmagedelestoico_77,psicologia / estoicismo,2025-07-08,41600,325,"0 (SB defasado; YouTube mostrou upload recente)",~10 min (um video visto),nao verificado,nao verificado,ES (faixa dublada en-US no video visto),"US$49-783",nao avaliado
Maquiavelo del Poder,https://www.youtube.com/@MaquiavelodelPoder,psicologia / Maquiavel,"2009-01-27 (conta antiga; SB)",24200,16,"SB sem coleta: marca o canal como banido/apagado, mas o canal esta no ar no YouTube",30 min a 2h,nao verificado,"voz de IA e imagens ilustrativas declaradas na descricao (confirmado na pagina do video)",ES/PT,"SB sem dados confiaveis",nao avaliado
Relatos para Dormir,https://www.youtube.com/@RelatosparaDormir23,historia para dormir,2025-12-02,14600,62,7,~3h15,nao verificado,nao verificado,ES,"US$99-1600",nao avaliado
Historias Para Dormir Oficial,https://www.youtube.com/@HistoriasParaDormir0125,historia para dormir,2025-11-04,60100,119,14,nao visivel,nao verificado,nao verificado,ES,"US$247-4000",nao avaliado
Historias Chatas Para Dormir,https://www.youtube.com/@Hist%C3%B3rias.Chatas.ParaDormir,historia para dormir,nao visivel,44600,128,nao visivel,~2h50,nao verificado,nao verificado,PT,nao consultado,nao avaliado
Wissen ist Macht,https://www.youtube.com/@WissenistMacht-y8o,historia para dormir,2025-05-23,5510,22,0,~1h34,nao verificado,nao verificado,DE,"US$30-478",nao avaliado
History and Mythology,https://www.youtube.com/@historyandmythologyEN,historia / mitologia narrada,2022-02-07,83600,478,9,nao visivel,nao verificado,nao verificado,EN (Shorts tambem em PT),"US$100-1600",nao avaliado
Actual Space,https://www.youtube.com/@Actualspace78,espaco / documentario,2023-01-10,55500,79,1,nao visivel,nao verificado,nao verificado,EN,"US$186-3000",nao avaliado
Paleora,https://www.youtube.com/@PaleoraSpace,espaco e paleontologia / documentario longo,2024-02-16,28100,136,3,1h28-2h27 ("Full Documentary"),nao verificado,nao verificado,EN + PT (titulos),"US$198-3200",nao avaliado
Historically,https://www.youtube.com/@HeyHistorically,historia dramatizada,2023-03-08,1530000,79,8,18-32 min,animacao propria (descricao: 100% HUMAN MADE; titulos com [No AI]),humana (declarado pelo canal),EN,"US$20000-319000",baixo (marca; nao replicavel)
```

---

## 3. Tabela de vídeos (CSV)

Campos da Fase 3. "formula_titulo" e "evergreen" são INFERÊNCIA minha; códigos: NUM = número, IMP = imperativo/segunda pessoa, NOME = nome do pensador, CUR = palavra de curiosidade (segredo, verdade, secreto), PERG = pergunta, FMT = formato repetido do canal, NOT = notícia em andamento. "gancho_30s" só onde li a transcrição; senão "nao verificado". Miniatura só foi descrita para o vídeo nº 1 de cada canal (ver seção 5 do arquivo consolidado); nos demais "nao vista". Likes: valor exibido (arredondado quando a tela arredonda).

```csv
canal,rank,titulo,url,views,data,duracao,likes,formula_titulo,evergreen,gancho_30s
Sleepy History Channel,1,"100 Sleepy Facts About the Seven Wonders of the World — Fall Asleep to History — No Adverts",https://www.youtube.com/watch?v=LheSNj9s__A,341584,2026-04-01,2:15:20,"2,7 mil",NUM+FMT,sim,"padrao do canal (video de 2025): cumprimento, resumo, pedido de like e comentario, transicao para o sono"
Sleepy History Channel,2,"100 Sleepy Facts About the First Humans — Fall Asleep to History — No Adverts",https://www.youtube.com/watch?v=5NW5qUMCQpI,304759,2026-04-08,2:19:54,2584,NUM+FMT,sim,nao verificado
Sleepy History Channel,3,"100 Sleepy Facts About Ancient Egypt — Fall Asleep to History — No Adverts",https://www.youtube.com/watch?v=Jm0kwGMZvXI,290878,2025-07-28,2:00:00,3089,NUM+FMT,sim,nao verificado
Sleepy History Channel,4 (recente),"Life In The Stone Age | Sleepy History",https://www.youtube.com/watch?v=b97NRrz1Rzg,163126,2026-09-19,2:54:00,888,tema+marca,sim,nao verificado
History Before Sleep,1,"👩‍🦰🏡 THE TRUTH About Women Who Lived Alone Without a Man 😴📜 History for Sleep",https://www.youtube.com/watch?v=Cv1vbJ_0VkQ,332206,2025-07-07,2:34:30,11957,CUR,sim,"esta noite vamos descobrir o segredo mais proibido da historia; 'e se eu dissesse que'; pede inscricao em menos de 30 s"
History Before Sleep,2,"🏛️🌒 Why Roman Cities were Abandoned in the Middle Ages 📜😴 | History for Sleep",https://www.youtube.com/watch?v=7l36GeKEkv8,291159,2025-07-29,2:44:31,4434,PERG,sim,nao verificado
History Before Sleep,3,"👒📏🤯 The WEIRDEST Etiquette Rules Victorian Women Had to Follow 😴📜 History Before Sleep",https://www.youtube.com/watch?v=n6eZq1VjWGw,258923,2025-08-16,3:04:04,5072,CUR,sim,nao verificado
History Before Sleep,4 (recente),"🕯️⚖️🏛️ Inside the Frightening 19th-Century Fat Farms for Wealthy Women 😴 | History for Sleep",https://www.youtube.com/watch?v=Krx3cmT5UIo,62321,2026-09-02,4:14:29,1710,CUR,sim,nao verificado
Sleepy Time Historian,1,"What Did Early Humans ACTUALLY Do All Day? | History for Sleep",https://www.youtube.com/watch?v=AHTEnwz0bL4,2719984,2025-12-31,2:15:36,29834,PERG+CUR,sim,"cena imersiva em 2a pessoa (acordar num abrigo de pedra); 11 capitulos; ritmo lento, sem promessa de segredo"
Sleepy Time Historian,2,"RH Negative Blood: The Secret SUPERPOWER That Lasts Till Today? History for Sleep",https://www.youtube.com/watch?v=luZ28uiieDo,1403962,2026-01-01,2:16:06,28454,CUR+PERG,sim,nao verificado
Sleepy Time Historian,3,"The Missing 100,000 Years: What Humans Did BEFORE Civilization | History for Sleep",https://www.youtube.com/watch?v=FEe4kEP2SqA,1055226,2025-12-22,2:21:34,12952,CUR,sim,nao verificado
History & Sleep,1,"Boring History For Sleep | Gentle Storytelling & Ambient Sounds (8 HOURS)",https://www.youtube.com/watch?v=8VtoYMPApvI,768320,2025-02-26,7:48:53,19733,FMT+duracao,sim,nao verificado
History & Sleep,2,"Boring History For Sleep | Gentle Storytelling & Ambient Sounds | (9 HOURS)",https://www.youtube.com/watch?v=MNbqnVJZPGo,174759,2025-02-23,7:53:35,5427,FMT+duracao,sim,nao verificado
History & Sleep,3,"Boring History For Sleep | Gentle Storytelling & Ambient Sounds | (7 HOURS)",https://www.youtube.com/watch?v=bsey8XUYmOw,171412,2025-03-21,7:45:20,4058,FMT+duracao,sim,nao verificado
History & Sleep,4 (recente),"What It Would Be Like To Time Travel To Medieval England | Boring History For Sleep",https://www.youtube.com/watch?v=6PnDGyX2QkE,18365,2026-08-21,5:54:25,192,PERG/hipotese,sim,nao verificado
Henry's History for Sleep,1,"The Secrets Victorian Nannies Took to Their Graves | History for Sleep",https://www.youtube.com/watch?v=V0na-XCeau4,33103,2026-07-12,2:13:40,895,CUR,sim,nao verificado
Henry's History for Sleep,2,"When the Family Left: Who Kept an Empty Victorian Mansion Alive? | History for Sleep",https://www.youtube.com/watch?v=9iUSNgCSCvQ,17617,2026-09-11,2:25:00,155,PERG,sim,nao verificado
Henry's History for Sleep,3,"Inside Victorian London's Most Horrific Workhouse Laundry | History for Sleep",https://www.youtube.com/watch?v=5uizjBavvAA,17215,2026-05-28,3:06:51,461,CUR,sim,nao verificado
Mindplicit,1,"Become So Disciplined It Scares Them - Machiavelli's Philosophy",https://www.youtube.com/watch?v=Lyl0DjiS5pQ,1846128,2025-12-06,21:08,51706,IMP+NOME,sim,"'existe uma versao sua que voce ainda nao conheceu... voce a temeria'; so nomeia Maquiavel por volta de 0:31"
Mindplicit,2,"How Intelligent People Deal with Stupid People — Schopenhauer",https://www.youtube.com/watch?v=4TspV1odsXo,1527517,2026-02-27,27:49,51513,PERG+NOME,sim,nao verificado
Mindplicit,3,"NEVER Explain Yourself. It Signals Weakness – Machiavelli",https://www.youtube.com/watch?v=GLLqBAuERJE,1143297,2025-12-04,18:48,34299,IMP+NOME,sim,nao verificado
Mindplicit,4 (recente),"Every Civilization Dies the Same Stupid Way — Spengler Predicted Ours",https://www.youtube.com/watch?v=SbcU9xP1ros,666795,2026-09-16,26:35,12758,CUR+NOME,sim,nao verificado
Dark Psychology Coded,1,"Never React, Never Explain, Just Ignore | Machiavelli's 7 Dark Psychology Tricks",https://www.youtube.com/watch?v=qncTXZXCeKU,2103981,2026-01-30,35:24,51553,IMP+NUM+NOME,sim,"acusacao em 2a pessoa ('voce entrega seu poder a vida inteira'); virada 'hoje isso acaba'; promete 7 truques"
Dark Psychology Coded,2,"8 Ruthless Lessons That Make You Dangerously Smart – Machiavelli",https://www.youtube.com/watch?v=HcZ6PsNWZqE,1755410,2025-08-28,41:46,37660,NUM+NOME,sim,nao verificado
Dark Psychology Coded,3,"How Machiavelli Would Outsmart Everyone – His 21 Laws of Power",https://www.youtube.com/watch?v=omatFPquFWw,1392204,2025-08-04,30:32,30326,NUM+NOME,sim,nao verificado
Dark Psychology Coded,4 (recente),"How to Outsmart People Before They Realize What You're Doing | Machiavelli's 10 Rules of Power",https://www.youtube.com/watch?v=ufCCZdB0TcQ,123435,2026-08-10,26:33,1546,NUM+NOME,sim,nao verificado
The Shadow Work,1,"Focus Only On Yourself (And Forget About Everyone Else) – Carl Jung",https://www.youtube.com/watch?v=WPQLz0rDZNk,1670803,2026-01-24,42:08,39766,IMP+NOME,sim,"pergunta empatica ('voce ja percebeu que esta se observando pelos olhos dos outros?'); so depois cita Jung; 9 capitulos"
The Shadow Work,2,"Think About This Before You Go To Sleep And Your Life Will Change – Carl Jung",https://www.youtube.com/watch?v=V8XQCkBa6Tk,1129993,2026-01-29,46:02,16914,IMP+NOME,sim,nao verificado
The Shadow Work,3,"Don't Force Anything, Let God Guide You – Carl Jung",https://www.youtube.com/watch?v=9_qtgvoGJuQ,1117066,2026-03-18,42:12,22334,IMP+NOME,sim,nao verificado
The Shadow Work,4 (recente),"The People Who Deserve Nothing — Carl Jung",https://www.youtube.com/watch?v=4EEALtiJols,255457,2026-08-28,45:25,2490,CUR+NOME,sim,nao verificado
Stoic Directions,1,"Always Be Silent In 9 Situations| Marcus Aurelius Stoicism",https://www.youtube.com/watch?v=auTrg1PEVXs,1757626,2024-05-24,41:34,42480,IMP+NUM+NOME,sim,"lamento ('a arte do silencio se perdeu'), pergunta retorica, definicao de estoicismo; 11 capitulos"
Stoic Directions,2,"MORNING STOICISM (LISTEN EVERY DAY) - Wake Up Early, Start Your Day Right | STOICISM",https://www.youtube.com/watch?v=4b8rMITRiVo,1352769,2026-02-04,51:37,26935,IMP,sim,nao verificado
Stoic Directions,3,"10 Stoic Rules That'll Will Manifest Everything You Want - EVERYTHING WILL COME TO YOU | STOICISM",https://www.youtube.com/watch?v=GaUExqfivQA,817296,2025-12-06,33:40,23162,NUM+IMP,sim,nao verificado
Stoic Directions,4 (recente; mesmo titulo do 3 republicado),"10 Stoic Rules That'll Will Manifest Everything You Want - EVERYTHING WILL COME TO YOU | STOICISM",https://www.youtube.com/watch?v=oJq2YkWLYKA,550200,2026-08-17,34:18,9427,NUM+IMP,sim,nao verificado
Crime Signal House,1,"Audio Engineer RESTORED Wiped Phone Recording —Nolan Wells' Final Words Caught on Tape!",https://www.youtube.com/watch?v=LlP__JJfzr4,376917,2026-09-26,30:10,10256,CUR+NOT,nao (noticia em andamento),nao verificado
Crime Signal House,2,"Courtroom Stunner Judge Moore Identifies Suspect Who Forced Open Nolan Wells' Phone!",https://www.youtube.com/watch?v=EHATyI-Wuu4,139418,2026-09-30,40:26,2998,NOT,nao,nao verificado
Crime Signal House,3,"BREAKING Nolan Wells Case Update — Warren Husdon COLLAPSES Under PRESSURE!",https://www.youtube.com/watch?v=bcO9vqzI52M,91972,2026-09-21,42:05,2155,NOT,nao,nao verificado
Crime Narrator,1,"The Oldest Cold Case Solved by a Single Drop of DNA",https://www.youtube.com/watch?v=kLZ9iZ1ajl8,458906,2026-03-27,24:45,15057,CUR+FMT,sim,nao verificado
Crime Narrator,2,"Florida 1981 Cold Case Solved — arrest shocks community",https://www.youtube.com/watch?v=UWqDDLYkbo0,379876,2026-01-24,37:30,9046,FMT (estado+ano),sim,nao verificado
Crime Narrator,3,"Missouri 1989 Cold Case Solved — arrest shocks community",https://www.youtube.com/watch?v=S8QeN5ofmQ4,231263,2026-01-22,25:36,5227,FMT (estado+ano),sim,nao verificado
Crime Narrator,4 (recente),"51 Years Later, DNA Exposed an Ohio Child Killer",https://www.youtube.com/watch?v=ei3Lw4031XM,34062,2026-07-22,28:54,1005,NUM+CUR,sim,nao verificado
True Crime Uncut,1,"How I Caught The BTK Killer",https://www.youtube.com/watch?v=-QPk0OkpuqI,1524431,2025-06-06,22:20,22624,1a pessoa,sim,nao verificado
True Crime Uncut,2,"Uncovering The Killer Clown's Crimes",https://www.youtube.com/watch?v=Df0tpIJf0O0,737281,2025-04-25,53:02,8446,tema,sim,nao verificado
True Crime Uncut,3,"Capturing America's Most Dangerous Serial Killer",https://www.youtube.com/watch?v=F3DVK7nkWXE,293884,2025-04-18,21:07,4545,superlativo,sim,nao verificado
True Crime Uncut,4 (recente),"Once Upon a Time... in Atlanta | Full True Crime Documentary",https://www.youtube.com/watch?v=HN-GLQzH9K4,221200,2026-09-10,55:06,2198,tema+rotulo documentario,sim,nao verificado
Unreal True Crime,1,"CAUTION!!! This Case Made ME Question HUMANITY - True Crime Documentary",https://www.youtube.com/watch?v=sqUw44QIpiA,943564,2026-06-19,27:02,7396,CUR+rotulo,sim,nao verificado
Unreal True Crime,2,"The Family Secret That Shocked an Entire Town - True Crime Documentary",https://www.youtube.com/watch?v=hLJ8JsD15H0,562647,2026-01-14,28:22,8391,CUR+rotulo,sim,nao verificado
Unreal True Crime,3,"What Happened Inside This Family's Home Shocked America - True Crime Documentary",https://www.youtube.com/watch?v=PPNgygVx49Q,455998,2025-12-14,27:47,3948,CUR+rotulo,sim,nao verificado
Unreal True Crime,4 (recente),"A Secret She Thought No One Would Ever Discover | True Crime Documentary",https://www.youtube.com/watch?v=WRUZc23hv0Y,430240,2026-07-14,27:30,1663,CUR+rotulo,sim,nao verificado
The Infographics Show - True Crime,1,"These True Crime Stories Are Too Dark For Bedtime",https://www.youtube.com/watch?v=QIH2ID53UKM,419746,2026-05-25,1:59:16,2779,compilacao,sim,nao verificado
The Infographics Show - True Crime,2,"The Navy SEAL Who Was Secretly A Brutal Murderer",https://www.youtube.com/watch?v=1rr_mggmEc0,369329,2026-05-07,32:37,8890,CUR,sim,nao verificado
The Infographics Show - True Crime,3,"The Secret Double Life of Los Angeles' Dirtiest Cop",https://www.youtube.com/watch?v=fwCE9kjkV8Q,349090,2026-03-01,27:04,7659,CUR,sim,nao verificado
The Infographics Show - True Crime,4 (recente),"The Journalist Serial Killer Who Reported on His OWN Crimes",https://www.youtube.com/watch?v=zjiOSGXL4FA,356122,2026-09-30,30:18,2106,CUR,sim,nao verificado
```

Nota: os 7 canais da Fase 5 (outros idiomas) não tiveram vídeos registrados neste formato; seus dados de views estão na seção 5.2.

---

## 4. Padrões vencedores

Força do sinal: **forte** = 3 ou mais canais diferentes; **fraco** = 1 ou 2 canais. Todos são INFERÊNCIA sobre dados OBSERVADOS.

| # | Padrão | Força | Evidência |
|---|---|---|---|
| 1 | Psicologia/filosofia: título em imperativo ou 2ª pessoa + nome do pensador após travessão ou barra | Forte | 4 de 4 canais do nicho |
| 2 | Número no título (regras, leis, truques, situações) | Forte | Mindplicit, Dark Psychology Coded, Stoic Directions |
| 3 | Abertura em 2ª pessoa (acusação, "e se eu dissesse", "imagine") | Forte | 5 canais de 2 nichos (7 aberturas lidas) |
| 4 | Sono: duração de 2 h ou mais e "for Sleep" no título | Forte | 5 de 5 canais acima de 2 h; "for Sleep" em 4 |
| 5 | Palavra de curiosidade no título (TRUTH, Secret, ACTUALLY, Shocked) | Forte | 7 canais de 2 nichos |
| 6 | True crime: 24–45 min | Forte | 5 canais |
| 7 | Miniatura com no máximo 3–4 palavras e um ponto focal | Forte | 6 canais |
| 8 | Tema evergreen | Forte | 13 de 14 canais (exceção: Crime Signal House) |
| 9 | Pico no começo e queda depois | Forte, com ressalva | 5 canais. **Ressalva**: vídeos recentes tiveram menos tempo para acumular views; a comparação não separa saturação de idade |
| 10 | Títulos exibidos em português a espectador brasileiro (indício de títulos multilíngues ou dublagem) | Forte como indício; trilhas de áudio não conferidas | 7 canais |
| 11 | Mesmo molde visual copiado entre canais (Mindplicit e Dark Psychology Coded) | Fraco (2 canais) | Também aparece nos clones em espanhol, como inferência não conferida |
| 12 | Marca/identidade própria associada a maior segurança (ilustração própria do The Shadow Work; produtos e identidade do Sleepy Time Historian) | Fraco (2 canais) | Inferência de risco, não medida |
| 13 | Shorts como aquisição: baixo alcance nos canais checados (ver 5.1) | Forte nos canais vistos, amostra pequena | 6 canais |
| 14 | Demanda por dublagem/localização do mesmo formato em ES, PT e DE (ver 5.2) | Forte para "história para dormir" (4 canais em 3 idiomas); fraco para psicologia (2 canais em ES) | Views de 400 mil a 1 mi em menos de 1 ano |

Anedotas (1 canal): "No Adverts" e selo "432 Hz" (Sleepy History Channel); selo "1.6M VIEWS" na miniatura e título republicado (Stoic Directions); emojis em todo título (History Before Sleep); 52 uploads em 30 dias (Sleepy Time Historian).

---

## 5. Fase 5: Shorts e dublagem

### 5.1 Shorts (OBSERVADO, 8 out 2026)

Não consegui ordenar Shorts por popularidade: o filtro "Shorts" da busca combinado com "Popularidade" devolveu lista vazia. O que segue é amostra das abas Shorts dos canais e de buscas por relevância, **não** um ranking dos Shorts mais vistos. Shorts virais fora dessa amostra podem existir.

| Canal / busca | Short | Views | URL |
|---|---|---|---|
| Dark Psychology Coded (aba Shorts) | "Perigosamente Confiante #maquiavel…" (título exibido em português) | 23 mil | https://www.youtube.com/shorts/CVwUgMcr6JA |
| Dark Psychology Coded | "The Desire to Please Kills Freedom #machiavellian…" | 17 mil | https://www.youtube.com/shorts/W0a-4-DXB88 |
| Stoic Directions | "7 Coisas Que Você Deve Sempre Manter Em Privado | Estoicismo" | 6,9 mil | https://www.youtube.com/shorts/rPY6fBZXg9E |
| Stoic Directions | "Aprenda estas lições de vida antes dos 40 #frases…" | 5,1 mil | https://www.youtube.com/shorts/-QBaNjctuzA |
| Busca "machiavelli dark psychology" (filtro Shorts) | "4 Machiavelli Tactics to Expose Hidden Motives" (canal não identificado) | 5,8 mil | https://www.youtube.com/results?search_query=machiavelli+dark+psychology&sp=EgIQCQ%253D%253D |
| Busca "history for sleep" | "Boring History: Fall Asleep to the Past" (canal não identificado) | 2,2 mil | https://www.youtube.com/results?search_query=history+for+sleep&sp=EgIQCQ%253D%253D |
| True Crime Uncut | "Os Assassinatos de Hillside" | 2,3 mil | https://www.youtube.com/shorts/mMm8vPHzY_4 |
| Busca "cold case solved" | maiores vistos: 931, 838 e 795 views; a maioria abaixo de 1 mil | — | https://www.youtube.com/results?search_query=true+crime+cold+case+solved&sp=EgIQCQ%253D%253D |

Outros fatos observados: Mindplicit, The Infographics Show – True Crime e Sleepy Time Historian não têm aba Shorts útil (Sleepy Time Historian: 1 Short de boas-vindas com 4.543 views); Dark Psychology Coded tem só 2 Shorts; Crime Narrator, 1 (480 views).

**Inferência:** nos canais e nichos checados, Shorts rendem de centenas a ~23 mil views, contra 100 mil a 2 mi dos vídeos longos dos mesmos canais. Isso é compatível com "Shorts como aquisição, não como receita", mas a amostra não prova que Shorts faceless não viralizem. Os canais grandes quase não investem em Shorts.

### 5.2 Dublagem e outros idiomas

**OBSERVADO** (busca "este ano", ordenada por popularidade, 8 out 2026):

| Idioma | Canal | Inscritos / vídeos | Vídeo visto | Views |
|---|---|---|---|---|
| ES, psicologia | EL MAGE DEL ESTOICO (https://www.youtube.com/@elmagedelestoico_77) | 41,6 mil / 326 | "Si juegan sucio, usa estos 10 trucos psicológicos de Maquiavelo" (https://www.youtube.com/watch?v=AUX76U3poPY) | 1 mi, há 8 meses |
| ES, psicologia | Maquiavelo del Poder (https://www.youtube.com/@MaquiavelodelPoder) | 24,2 mil / 16 | "8 Lecciones de Maquiavelo Para Volverte Peligrosamente Inteligente" (https://www.youtube.com/watch?v=5b8Pa6ai060); outros vídeos do canal de 1,1 mil a 41 mil | 1 mi, há 8 meses |
| ES, sono | Relatos para Dormir (https://www.youtube.com/@RelatosparaDormir23) | 14,6 mil / 62 | "¿Cómo Era un Día Completo en la Edad Media? \| Historia Para Dormir" | 1 mi, há 8 meses |
| ES, sono | Historias Para Dormir Oficial (https://www.youtube.com/@HistoriasParaDormir0125) | 60,1 mil / 120 | "SÉNECA \| El Filósofo que Crio a un Monstruo \| HISTORIA PARA DORMIR" | 556 mil, há 7 meses |
| PT, sono | Histórias Chatas Para Dormir (https://www.youtube.com/@Hist%C3%B3rias.Chatas.ParaDormir) | 44,6 mil / 128 | "Desde QUANDO as Pessoas Fumam MACONHA?" (2:50:35) | 401.725, há 11 meses |
| PT, sono | The Sleepy Astronomer PT (https://www.youtube.com/@TheSleepyAstronomerPT) | não consultado | "Por Que Nunca Sairemos Da Nossa Galáxia \| Documentário Para Dormir" | 235 mil, há 11 meses |
| DE, sono | Wissen ist Macht (https://www.youtube.com/@WissenistMacht-y8o) | 5,53 mil / 22 | "Das Deutsche Mittelalter – Geschichte zum Einschlafen (800–1500)" | 413 mil, há 10 meses; outro vídeo do canal com 1 mil, há 2 meses |

Leituras:
- A descrição de "Maquiavelo del Poder" em um vídeo (trecho visto na busca) declara "voces en off de IA e imágenes ilustrativas". Ou seja, canais com voz de IA declarada acumulam 1 mi em um vídeo. Não verifiquei se o canal está monetizado.
- **INFERÊNCIA:** o formato "história para dormir" já foi copiado em espanhol, português e alemão, com canais de 5 mil a 60 mil inscritos e vídeos de 400 mil a 1 mi. O espaço não está vazio. Em alemão achei só 1 canal pequeno; **[Suposição]** pode haver mais espaço lá, mas foi uma única busca.
- Os títulos de canais grandes em inglês aparecem em português para mim: possível dublagem ou título multilíngue (trilhas não conferidas).

**TERCEIROS (RPM por idioma).** Lenostube (página sem data; resultado de busca, não li a página inteira): RPM estimado alemão US$3,04, espanhol US$1,65, japonês US$1,61, português US$1,10, hindi US$0,26; CPM alemão US$5,53, japonês US$2,93, espanhol US$3,00, português US$2,00, hindi US$0,82. Coreano: não achei. AIR Media-Tech (2025, secundário): CPM Japão US$2,84 e Coreia US$2,86. VideoDubber (2026) dá faixas bem maiores para japonês (US$6–18) sem citar base; peso baixo. AIR também diz ~3,1 mi de criadores em espanhol contra ~246 mil em hindi. **Fontes discordam e vários desses sites vendem tradução; trate como ordem de grandeza.** Fontes: https://www.lenostube.com/en/youtube-cpm-rpm-rates/, https://air.io/en/audience-growth/what-are-the-most-popular-languages-on-youtube, https://videodubber.ai/blogs/top-languages-to-translate-videos/amp/.

**Documentação oficial** (resumida em [youtube-faixas-audio-dublagem.md](youtube-faixas-audio-dublagem.md)): dublagem automática aberta a todos desde fev/2026, vídeos até 120 min, não editável; faixa de áudio própria só pelo Studio no desktop e com acesso "disputado" entre páginas oficiais; nada lido liga dublagem à política de monetização.

**INFERÊNCIA para o plano:** por RPM de terceiros, alemão > espanhol ≈ japonês > português > hindi; por concorrência observada, ES e PT já têm clones. Dublar vídeos de 2 h para fora do limite de 120 min da dublagem automática exigiria faixa própria (desktop).

---

## 6. Fase 6: riscos e saturação

**(1) Política atual:** ver [fase6-politica-youtube.md](fase6-politica-youtube.md) (páginas oficiais de monetização, divulgação de conteúdo sintético e YPP, lidas em 8 out 2026). Resumo: slideshow de imagens com pouca narrativa e conteúdo de IA com "templates genéricos" estão na lista de não monetizáveis; avaliação do canal inteiro; divulgar IA não afeta monetização.

**(2) Relatos de canais removidos ou desmonetizados (TERCEIROS, todos secundários):**
- Kapwing (nov/2025) classificou canais como "AI slop"; segundo Tubefilter (29 jan 2026, citando Kapwing), ao menos 18 desses canais foram apagados ou tiveram vídeos ocultados. Exemplos citados: CuentosFacianantes (vídeos de tema Dragon Ball, 1,2 bi de views antes de sumir) e Imperio de Jesus (conteúdo religioso de IA, estava no Global Top 50 do Tubefilter). https://tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/
- O mesmo artigo não traz declaração de porta-voz nem política nomeada; a única fala do YouTube citada é a carta aberta de Neal Mohan sobre combater spam, clickbait e conteúdo repetitivo. Uma outra busca resumiu que um porta-voz confirmou "spam e práticas enganosas"; **não confirmei isso na página**, tratar como não verificado.
- Contagens variam por fonte (11 a 18 canais; "16 canais, 35 mi de inscritos"). Um caso de canal bíblico de 588 mil inscritos e US$30 mil/mês desmonetizado vem de um único blog de ferramenta; não verificado.
- Sinais de risco que as fontes repetem: slideshow com pouca edição, clones em que só o título muda, cadência de dezenas de vídeos por dia, reupload de vídeo alheio, playlists de música de IA com imagem estática, avaliação do canal inteiro.
- Fontes com viés comercial (vendem ferramentas): fliki.ai, invideo.io, outlierkit.com, scalelab.com, milx.app, air.io.

**(3) Nichos mais citados:** infantil/animais de IA, receitas narradas por IA, fan content de anime, conteúdo religioso/bíblico e trailers falsos de filmes (Search Engine Journal e resumos da busca; não abri a página do SEJ). **Nenhuma fonte lida cita "história para dormir", psicologia ou true crime como alvo de remoção**, mas isso é ausência de evidência: não procurei esses nichos especificamente em relatos de remoção, e não verifiquei se os 14 canais estudados estão monetizados.

---

## 7. Top 3 nichos recomendados (2 h/semana)

Critério: demanda observada, viabilidade com 1 vídeo por semana e menor choque com a política. **Nenhum é seguro**; os dois primeiros só funcionam com autoria real.

**1. História narrada com tese própria e acervo real (25–45 min, evergreen).** Demanda: vídeos longos de história lideram em três canais (Sleepy Time Historian 2,7 mi; History and Mythology 83,6 mil inscritos e 478 vídeos; Sleepy History 340 mil). Risco: médio se misturar acervo de domínio público (pipeline `documentary-montage`) com ilustração e uma tese por vídeo. Ideias (fatos a conferir em fonte primária antes de roteirizar, pela regra do projeto):
- "Por que a peste negra elevou salários na Inglaterra": tese econômica, com fontes de registros de salário.
- "Colapso da Idade do Bronze: três explicações e o que a evidência sustenta".
- "Como os aquedutos romanos funcionavam e por que a manutenção, não a invasão, decidiu o fim de muitos".

**2. Psicologia/filosofia aplicada, com leitura do texto original (20–40 min).** Demanda: melhor sinal de canal novo (Mindplicit, Dark Psychology Coded) e adaptações em ES com 1 mi de views. Risco alto pela saturação e pelo molde idêntico; o The Shadow Work, com ilustração própria, é o modelo menos exposto. Diferencial possível: citar o texto primário e discordar. Ideias:
- "O que Schopenhauer realmente escreveu sobre solidão, comparado ao que circula nas redes".
- "Príncipe, cap. 17: é melhor ser temido do que amado? Lendo o trecho".
- "Jung e a sombra: três coisas que ele disse e três que atribuem a ele".

**3. História para dormir (2 h ou mais), como formato derivado do nº 1.** Demanda comprovada em EN, ES, PT e DE; produção barata (mesma pesquisa do nº 1). Risco médio-alto, por ser o formato mais próximo de "imagens + voz"; só como complemento, não como canal único, e com roteiro autoral. Ideias:
- "Um ano numa aldeia inglesa medieval, estação por estação".
- "O dia de um legionário romano no Muro de Adriano".
- "A rotina a bordo de um navio na Era da Vela".

Fora do top 3: **finanças** tem o maior CPM de terceiros (US$15–45), mas nenhum canal novo verificado; fica como hipótese a testar, não recomendação.

**Não deu para verificar:** tipo de voz de qualquer canal (nenhum áudio ouvido); se os canais citados estão monetizados e como o YouTube os trata; RPM real; trilhas de áudio dubladas; ciência, espaço, animais, biografias, tech e lifestyle (não pesquisados); Shorts mais vistos de cada nicho (não consegui ordenar).

---

## 8. Limitações

1. **Social Blade:** bloqueado na 1ª tentativa, liberado na 2ª (seção 9). Continua sem dados: Histórias Chatas Para Dormir (a URL do handle deu 404 no Social Blade) e Maquiavelo del Poder (o Social Blade o marca como banido/apagado, mas o canal está no ar no YouTube; conflito não resolvido).
2. **Sem áudio:** tipo de voz (humana, TTS, clonada) não verificado em nenhum canal, salvo declaração do canal (Sleepy Time Historian, Maquiavelo del Poder, Unreal True Crime, Historically).
3. **Transcrição:** lida em 9 vídeos; nos demais o painel não carregou ou veio vazio.
4. **Shorts:** amostra sem ordenação por views.
5. **RPM:** não existe dado público; os valores são de Social Blade (faixa fixa), OutlierKit ("planning estimates"), Lenostube (sem data), AIR e VideoDubber (secundários e comerciais). Não li as páginas dessas três últimas por inteiro, só resumos de busca.
6. **Pico e queda:** comparar top-3 com recentes mistura saturação com idade do vídeo.
7. **Inconsistência da Fase 1:** o "líder com 20 meses" não bate com as datas observadas (Sleepy History Channel ~14 meses; Sleepy Time Historian ~32).
8. **Crime Signal House:** a linha do Social Blade está defasada (73,6 mil views em 30 dias contra 939 mil no total).
9. **Remoções de canais:** números de fontes secundárias, com viés comercial e divergentes entre si. Nenhum canal estudado teve o status de monetização verificado.
10. **Cobertura de nichos:** só 3 nichos com cobertura completa. Geopolítica, mitologia, mistérios e finanças: uma busca cada, dominada por criadores com rosto, sem conclusão sobre faceless.
11. **Conta logada no Brasil:** resultados personalizados, títulos de canais em inglês aparecem traduzidos para o português.

---

## 9. Segunda tentativa nas lacunas (8 out 2026)

O que não tinha dado certo foi refeito. **Resolvido**: Social Blade, faixas de áudio dubladas, declaração de IA nas descrições, nichos extras. **Parcial**: aberturas, Shorts. **Não resolvido**: tipo de voz, monetização real.

### 9.1 Social Blade (OBSERVADO como página; valores de receita são TERCEIROS)

| Canal | Criado | Inscritos | Vídeos | Views totais | Views 30 dias | Uploads 30 dias | Receita SB (TERCEIROS) |
|---|---|---|---|---|---|---|---|
| EL MAGE DEL ESTOICO (ES) | 8 jul 2025 | 41,6 mil | 325 | 3,0 mi | 196 mil | 0 (SB defasado) | US$49–783/mês |
| Relatos para Dormir (ES) | 2 dez 2025 | 14,6 mil | 62 | 2,75 mi | 397 mil | 7 | US$99–1,6 mil/mês |
| Historias Para Dormir Oficial (ES) | 4 nov 2025 | 60,1 mil | 119 | 10,1 mi | 989 mil | 14 | US$247–4 mil/mês |
| Wissen ist Macht (DE) | 23 mai 2025 | 5,51 mil | 22 | 666 mil | 119 mil | 0 | US$30–478/mês |
| History and Mythology (EN) | 7 fev 2022 | 83,6 mil | 478 | 9,9 mi | 400 mil | 9 | US$100–1,6 mil/mês |
| Actual Space (EN, espaço) | 10 jan 2023 | 55,5 mil | 79 | 9,0 mi | 744 mil | 1 | US$186–3 mil/mês |
| Paleora (EN/PT, espaço e paleontologia) | 16 fev 2024 | 28,1 mil | 136 | 7,7 mi | 791 mil | 3 | US$198–3,2 mil/mês |
| Historically (EN, história dramatizada) | 8 mar 2023 | 1,53 mi | 79 | 455 mi | 79,7 mi | 8 | US$20 mil–319 mil/mês |
| Maquiavelo del Poder (ES) | 27 jan 2009 (conta antiga) | 18,8 mil (SB defasado; YouTube: 24,2 mil) | 16 | 931 mil | sem coleta | sem coleta | SB diz "banned or deleted"; canal está no ar no YouTube |

URL base: https://socialblade.com/youtube/handle/ seguido do handle. Histórias Chatas Para Dormir: 404 no Social Blade.

**Leituras (INFERÊNCIA):**
- Os 3 canais de "história para dormir" em espanhol nasceram em nov–dez 2025 e já têm 14,6 a 60,1 mil inscritos; Historias Para Dormir Oficial tem 10,1 mi de views em ~11 meses e +4 mil inscritos nos últimos 30 dias. **O mercado ES de sono-história é novo e ativo, não vazio.** [Provável] Dublar o formato para espanhol é viável como mercado, mas a concorrência já está crescendo.
- Wissen ist Macht (DE): 5,5 mil inscritos, 22 vídeos, vídeos de 400 mil a 1 mi de views. Em alemão uma busca achou só esse canal. [Suposição] Pode haver espaço; amostra de 1 canal.
- Espaço/documentário longo: Actual Space e Paleora têm 744 mil e 791 mil views em 30 dias com 55 e 28 mil inscritos (muita view por inscrito). Ambos têm mais de 18 meses, então não são "novos". Não sei se usam voz ou imagem de IA. Paleora publica "Full Documentary" de 1h28 a 2h27. Candidato fraco: dados do SB e dois canais.
- Historically: 1,53 mi de inscritos com 79 vídeos, 79,7 mi de views em 30 dias, vídeos de 18 a 32 min com títulos terminados em "[No AI]" e descrição "(100% HUMAN MADE)". O vídeo de 32 min tem 5,3 mi de views (https://www.youtube.com/watch?v=fXuWQg7uJKg). É marca com animação e humor próprios, não replicável por script. **O que importa:** um dos maiores outliers de história do período usa "No AI" como argumento de venda, sinal de risco de posicionamento para um canal de IA.

### 9.2 Faixas de áudio dubladas (OBSERVADO nos dados do player de cada vídeo)

Contei as faixas de áudio expostas na página do vídeo mais visto de cada canal. A lista de idiomas de Mindplicit coincide com a lista oficial de dublagem automática do inglês (ver [youtube-faixas-audio-dublagem.md](youtube-faixas-audio-dublagem.md)); a página não diz se a faixa é automática ou enviada pelo canal, então "dublagem automática" é **INFERÊNCIA [Provável]**.

| Canal (vídeo mais visto) | Faixas dubladas (além do original) |
|---|---|
| Mindplicit | 17: ar, bn, de, es, fr, hi, id, it, he, ja, ko, ml, nl, pl, pt-BR, ru, uk |
| Unreal True Crime | 20 (ar, bn, de, es, fr, hi, id, it, he, ja, ko, ml, nl, pa, pl, pt-BR, ru, ta, te, uk) |
| True Crime Uncut | 12 (de, es, fr, hi, id, it, ja, ml, nl, pl, pt-BR, uk) |
| The Shadow Work | 7 (de, es, fr, hi, id, it, pt-BR) |
| Infographics Show – True Crime | 7 (de, es, fr, hi, id, it, pt-BR) |
| Stoic Directions | 7 (mesmo número que o TSW; lista exata não registrada) |
| EL MAGE DEL ESTOICO (original em espanhol) | 1: inglês (en-US) |
| Sem faixas dubladas | Sleepy History Channel, History Before Sleep, Sleepy Time Historian, History & Sleep, Henry's, Dark Psychology Coded, Crime Narrator, Crime Signal House, Historically, Maquiavelo del Poder |

Leituras:
- **Os canais com títulos exibidos em português (Fase 4, padrão 10) têm faixas dubladas** em Mindplicit, True Crime Uncut, Unreal True Crime, The Shadow Work, Infographics e Stoic Directions. O padrão 10 passa de indício a observação para esses 6. Dark Psychology Coded mostrou título traduzido, mas o vídeo mais visto não tem faixas.
- Os vídeos de 2 h ou mais dos canais de sono (todos acima de 120 min) não têm dublagem, o que **bate com o limite oficial de 120 min** da dublagem automática. **[Provável]** Para dublar vídeo de sono é preciso faixa própria, enviada pelo desktop.
- Há dublagem do espanhol para o inglês (EL MAGE DEL ESTOICO), então o fluxo inverso também é usado.

### 9.3 Declarações de IA e fonte do conteúdo (OBSERVADO nas descrições do vídeo mais visto)

Busquei termos de IA/sintético/gerado nas descrições de 12 vídeos. **Ausência de menção não prova ausência de IA.**
- **Unreal True Crime:** a descrição diz que o canal "may use AI-generated voice technology as a production tool". Tem links de afiliado da Amazon. É o único canal de true crime com voz de IA declarada.
- **Maquiavelo del Poder (ES):** "este video utiliza voces en off de IA e imágenes ilustrativas", confirmado na página do vídeo de 1 mi de views (https://www.youtube.com/watch?v=5b8Pa6ai060).
- **Sleepy Time Historian:** link na descrição para ferramenta de vídeo com IA (autotube.pro).
- **True Crime Uncut:** a descrição do vídeo mais visto abre com "Welcome to 'Questions With'" e apresenta um detetive que "shares his expert insight". Reforça a leitura de que o canal publica entrevistas (INFERÊNCIA já marcada na seção 2); não verifiquei de quem são os direitos.
- Sem menção a IA: Sleepy History Channel, History Before Sleep, Mindplicit, Dark Psychology Coded, The Shadow Work, Stoic Directions, History & Sleep, Henry's, Crime Signal House, Crime Narrator, Infographics.

### 9.4 Monetização: sinal indireto, inconclusivo

Contei os pontos de anúncio (ad placements) nos dados do player: Historically 17; The Shadow Work 20; Stoic Directions 15; Infographics 22; True Crime Uncut 7; Unreal True Crime 14; Sleepy Time Historian 28; History & Sleep 221; Henry's 63; Crime Signal House 1; **zero** em Sleepy History Channel, History Before Sleep, Mindplicit, Dark Psychology Coded, Crime Narrator, EL MAGE e Maquiavelo del Poder. Um vídeo de controle (Rick Astley, monetizado) mostrou 1.

**Não dá para concluir monetização com isso.** Zero em Mindplicit e Dark Psychology Coded (mais de 250 mil inscritos, quase certamente no YPP) mostra que o sinal falha. Coincidência a conferir: o Sleepy History Channel traz "No Adverts" no título e tem zero. A única forma de saber o status de monetização é o Studio do próprio canal. **Lacuna que continua aberta.**

### 9.5 Aberturas (transcrição) e Shorts

- **Crime Narrator, mais visto** (https://www.youtube.com/watch?v=kLZ9iZ1ajl8): abre com uma frase seca sobre a idade e o peso de uma criança, data de 1959, vira o enquadramento (não é a história de uma criança que se perdeu, é a de um predador) e promete o arco: 62 anos, três gerações de detetives e um pote de vidro num depósito de provas. Tem capítulos. Padrão: gancho de fato, enquadramento e promessa de desfecho.
- **Sleepy History Channel, mais visto atual** (https://www.youtube.com/watch?v=LheSNj9s__A): cumprimento fixo do canal, "esta noite viajamos por desertos e mares", resumo poético do tema, sem tese; confirma o molde de 2025.
- True Crime Uncut, Crime Signal House, Unreal True Crime, Infographics, History & Sleep, Henry's: **continuam não verificados** (painel de transcrição vazio ou sem carregar; a via por API voltou vazia).
- **Shorts, amostra ampliada:** History and Mythology: 19 mil (Apófis), 7,6 mil (Medusa), 2,7 mil, 2,6 mil, 2,1 mil, 1,4 mil. O maior Short visto continua sendo 23 mil (Dark Psychology Coded). A ordenação por popularidade de Shorts continua indisponível.

### 9.6 Nichos que faltavam

| Nicho | Resultado (busca "este ano", ordem por popularidade) |
|---|---|
| Espaço/ciência | Actual Space e Paleora (9.1); STORY ADDICTION com 27 mil num vídeo. Candidato fraco. |
| Animais | Topo é BBC Earth (3,7 mi) e Nat Geo Animals (1,7 mi). Nenhum faceless pequeno apareceu. |
| Biografias / história geral | Historically (9.1); History Industry (hindi, 11 mi). |
| Finanças/negócios | Statrys (marca fintech, 9,5 mi) e Ankul Rajpurohit (4,1 mi; não verifiquei se aparece em vídeo). Nenhum faceless novo. |
| Lifestyle "top 10" de luxo | Poucas views (centenas), exceto um vídeo de 12 mi sobre arte (Stay Wild, formato não verificado). Sem sinal. |
| Tech/IA | Topo é tutorial de IA com 3,6 mi (Sandeep Goswami) e conteúdo religioso. Sem canal faceless de tech com sinal. |

### 9.7 O que continua sem resposta

1. **Tipo de voz** (humana, TTS, clonada): só declarações em descrição; ouvir áudio não é possível por esta via.
2. **Monetização real** dos canais: só se vê no Studio do dono.
3. **RPM real**: sem dado público.
4. **Aberturas** de 6 canais e Shorts ordenados por views.
5. **Histórias Chatas Para Dormir** (Social Blade 404) e **Maquiavelo del Poder** (Social Blade o dá como banido/apagado; o YouTube o mostra no ar).
6. **Se Actual Space e Paleora são faceless produzidos por IA**: não verifiquei.

### 9.8 Efeito sobre o top 3 (seção 7)

Ranking mantido, com dois ajustes: (a) **nº 3, história para dormir**, ganha evidência de mercado novo em ES (canais de nov/dez 2025 já com 15 a 60 mil inscritos), mas os vídeos de 2 h ou mais ficam fora da dublagem automática; (b) o **risco de posicionamento de IA** sobe: o maior outlier de história do período se vende como "[No AI]". Espaço/ciência em documentário longo entra como candidato a verificar, não como recomendação.
