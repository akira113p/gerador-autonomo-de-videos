"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v2-dia-em-roma/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v2-dia-em-roma/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro",
    "1": "What was an hour in Rome?",
    "2": "Waking up in an insula",
    "3": "Breakfast and school",
    "4": "Hours 1-2: the morning greeting",
    "5": "Hour 3: the courts",
    "6": "Until hour 5: work, lunch and garum",
    "7": "Hour 6: the original siesta",
    "8": "Hour 7: walls that talk",
    "9": "Hours 8-9: the baths",
    "10": "Hours 9-10: dinner",
    "10b": "Days off: bread and circuses",
    "11": "Night",
    "12": "What's still with us",
}

TOPO = """A day in ancient Rome, hour by hour: what ordinary Romans actually did from sunrise to nightfall, in their own words.

Around 90 AD, the poet Martial left us a schedule of the Roman day, hour by hour. We follow it from before sunrise to after dark: crowded apartment blocks, schoolmasters shouting before the roosters, the morning greeting, lawyers timed by water clocks, urine taxes, street food, graffiti, noisy baths, long dinners and dark, dangerous streets.

Every quote in this video comes from an ancient source, translated for this video. Sources are listed below."""

FONTES = """SOURCES (ancient texts and inscriptions)
- Martial, Epigrams 4.8 (the hours of the Roman day), 14.223 (breakfast), 9.68 (the schoolmaster), 7.83 (the slow barber), 1.59, 3.7, 10.70, 10.75 (the sportula)
- Pliny the Elder, Natural History 7.212-215 (sundials and water clocks), 28.66 (fullers and urine), 31.93-94 (garum), 36.102 (Circus Maximus)
- Aulus Gellius, Attic Nights 3.3.5 (the comedy attributed to Plautus that curses the sundial)
- Juvenal, Satires 1.95-96 and 1.120-121 (sportula), 3.190-202, 3.232-248, 3.268-285 (buildings, noise, crowds, night), 6.447, 10.77-81 (bread and circuses)
- Strabo, Geography 5.3.7 (Augustus' height limit)
- Tabula Heracleensis, lines 56-61 (daytime wagon ban)
- Frontinus, On the Aqueducts 1.16
- Pliny the Younger, Letters 1.15 (the missed dinner), 2.11.14 (a five-hour speech), 2.14 (paid applause), 9.6 (the races)
- Suetonius, Vespasian 23.3 (the urine tax); Augustus 25 and 30, Cassius Dio 55.26 (the vigiles)
- Seneca, Letters 15.4, 56 (living above a bath), 70.20, 86.9
- Horace, Satires 1.3.6-7 (ab ovo usque ad mala), 1.3.137
- Macrobius, Saturnalia 1.16.34 (market days)
- Dionysius of Halicarnassus, Roman Antiquities 3.68 (Circus Maximus)
- Petronius, Satyricon 26 (Trimalchio's clock)
- Lex metalli Vipascensis, CIL II 5181 (bath hours and prices)
- Pompeii inscriptions: CIL IV 576, 581 (Vatia), 1842 (Pumidius Dipilus), 1904, 2461, 2487 ("I'm amazed, O wall"), 4957
- Parco Archeologico di Pompei, Regio V thermopolium excavation (December 2020)

Population figures for ancient Rome are modern estimates and vary between scholars.

Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#AncientRome #RomanHistory #History"


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def main() -> None:
    sufixo = os.environ.get("SUFIXO", "")
    tempos = json.loads((AQUI / f"tempos{sufixo}.json").read_text(encoding="utf-8"))
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    linhas = []
    for c in cenas:
        if c["inicio_capitulo"]:
            t = 0 if c["id"] == "001" else tempos["cenas"][c["id"]]
            linhas.append(f"{mmss(t)} {CAPITULOS[c['capitulo']]}")
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{FONTES}\n{MUSICA[sufixo]}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / f"descricao{sufixo}.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
