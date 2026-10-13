"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v5-revolucao-francesa/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v5-revolucao-francesa/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: what's the date today?",
    "1": "A new calendar, a new world",
    "2": "Waking up before sunrise",
    "3": "Getting dressed: clothes as politics",
    "4": "The bread line (5 a.m.)",
    "5": "On the way to work (7 a.m.)",
    "6": "Work in the morning",
    "7": "Lunch and \"what are you worth?\" (noon)",
    "8": "The afternoon: what changed for women",
    "9": "Late afternoon: the carts",
    "10": "Lavoisier, the man who measured the world",
    "11": "Night: the section assembly",
    "12": "The end of the Terror",
}

TOPO = """What was daily life like during the French Revolution? We follow one ordinary day in Paris, 19 Floréal, Year II (8 May 1794), at the height of the Terror, through the eyes of a carpenter from the Faubourg Saint-Antoine.

A calendar with ten-day weeks and a clock with ten hours, bread lines before dawn, price controls, clothes that could get you arrested, a new way of speaking to strangers, and the day the chemist Antoine Lavoisier, who helped create the metric system, was executed. The guillotine is never shown."""

FONTES = """SOURCES
- Decree of 4 Frimaire Year II (the republican calendar and decimal time); Fabre d'Églantine's report; Musée des Arts et Métiers
- Archives parlementaires de la Révolution française (Convention debates and decrees: the Republic, the Maximum, the Law of Suspects, hoarding, the sections, citizenship)
- Ken Alder, The Measure of All Things (2002) (the metric system)
- Albert Soboul, The Parisian Sans-Culottes and the French Revolution (1964); George Rudé, The Crowd in the French Revolution (1959)
- Louis-Sébastien Mercier, Tableau de Paris (1781-88); Daniel Roche, The People of Paris (1987)
- Steven Kaplan, The Bakers of Paris and the Bread Question (1996)
- Laurent Dubois, Avengers of the New World (2004)
- Roderick Phillips, Putting Asunder: A History of Divorce in Western Society (1988)
- Decree of 9 Brumaire Year II (women's clubs); Revolutionary Tribunal records
- Henri Wallon, Histoire du Tribunal révolutionnaire de Paris (1880-82)
- Peter McPhee, Robespierre: A Revolutionary Life (2012)
- Jean-Pierre Poirier, Lavoisier: Chemist, Biologist, Economist (1996); Lavoisier, Traité élémentaire de chimie (1789)
- Metropolitan Museum of Art: Jacques-Louis David's portrait of Lavoisier and his wife (1788)
- Delambre, "Notice sur la vie et les ouvrages de M. le comte J.-L. Lagrange" (1812)
- Donald Greer, The Incidence of the Terror During the French Revolution (1935)
- Harris, The Assignats (1930)

Some details of ordinary life are reconstructed from general accounts; the carpenter and his family are fictional.
Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#FrenchRevolution #History #Paris"


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
