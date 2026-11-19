"""Monta a descrição do YouTube (inglês) com capítulos, licença CC BY-SA do Backrooms Wiki, fontes, créditos e hashtags.
Rode depois do montar.py.

  python piloto/v14-backrooms/gerar_descricao.py        # tempos.json -> descricao.md

Limite de 5000 caracteres; capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais.
"""

import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "You don't make it out", "1": "Hour 1: Level 0", "2": "Hour 9: walking in circles", "3": "Day 3?",
    "4": "Level 1: the Habitable Zone", "5": "Week 3: Base Alpha", "6": "Day 200?: the expedition",
    "7": "Level 3: the Electrical Station", "8": "The bars", "9": "The log",
}

TOPO = """What would your life be like if you fell into the Backrooms? From the first hour in Level 0 to a M.E.G. expedition into Level 3, every rule in this story comes from the Backrooms Wiki, and the real science behind it (walking in circles, losing track of time, why fluorescent lights hurt) comes from published studies."""

LICENCA = """LICENSE
Content relating to the Backrooms is licensed under Creative Commons Sharealike 3.0 and all concepts originate from http://backrooms-wiki.wikidot.com/ and its authors. This video, being derived from this content, is hereby also released under Creative Commons Sharealike 3.0.

Pages used (Backrooms Wiki, CC-BY-SA-3.0):
- "Level 0 - Threshold" by DivineAtlas, DrAkimoto and RobertGoerman - https://backrooms-wiki.wikidot.com/level-0
- "Level 1 - Habitable Zone" by Praetor3005 and DivineAtlas - https://backrooms-wiki.wikidot.com/level-1
- "Level 2 - Abandoned Utility Halls" by Greggita Mahayfaio - https://backrooms-wiki.wikidot.com/level-2
- "Level 3 - Electrical Station" by Natedagreat563 - https://backrooms-wiki.wikidot.com/level-3
- "Base Alpha" by Praetor3005 - https://backrooms-wiki.wikidot.com/base-alpha
- "The M.E.G." by Greggita Mahayfaio, Natedagreat563, Orb1t41, Poliacci, Positive123, Praetor3005, Robert Goerman, Reyday, Snomwriting and Squibblezombie - https://backrooms-wiki.wikidot.com/the-m-e-g
- "Object 1 - Almond Water" by Natedagreat563 - https://backrooms-wiki.wikidot.com/object-1
- "Entity 3 - Smilers" by Palico22, rewritten by Stretchsterz - https://backrooms-wiki.wikidot.com/entity-3
- "Entity 5 - Clumps" - https://backrooms-wiki.wikidot.com/entity-5
- "Entity 10 - Skin-Stealers" - https://backrooms-wiki.wikidot.com/entity-10
- "Entity 67 - Partygoers" by Robert Goerman and MC_Crafter_24_7 - https://backrooms-wiki.wikidot.com/entity-67
- FAQ - https://backrooms-wiki.wikidot.com/faq
Original Backrooms concept: anonymous 4chan /x/ post, May 2019. Original photo (CC0): Bob Mazza / HobbyTown USA of Oshkosh.
The expedition, the characters and the ending are our own story, built on the wiki's rules."""

FONTES = """SCIENCE SOURCES
- Wilkins et al., "Fluorescent lighting, headaches and eyestrain", Lighting Research & Technology 21 (1989)
- Diel & Lewis, "Structural deviations drive an uncanny valley of physical places", J. Environmental Psychology 82 (2022)
- Souman et al., "Walking straight into circles", Current Biology 19 (2009)
- Armstrong et al., J. Nutrition 142 (2012); Ganio et al., British J. Nutrition 106 (2011)
- Michel Siffre's 1962 cave experiment (Cabinet magazine interview; Boston Globe, 2024)
- Radvansky & Copeland, Memory & Cognition 34 (2006); Radvansky et al., Q. J. Experimental Psychology 64 (2011)
- 404 Media (2024) on the origin of the Backrooms photo

Illustrations: AI-generated in a custom style. Narration: synthetic voice."""

MUSICA = """MUSIC
Music provided by NCMFYT
Mix: psylokid, dj akeeni - endless maze
Watch on YouTube: https://bit.ly/4yVCKb9
"Bass Walker" by Kevin MacLeod (incompetech.com), licensed under CC BY 3.0 (creativecommons.org/licenses/by/3.0)
"Dark Ambient - Horror Background Music No Copyright" by THRLL, https://www.youtube.com/watch?v=oO0DvpIWhd0"""

HASHTAGS = "#Backrooms #Level0 #LiminalSpaces"


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def main() -> None:
    tempos = json.loads((AQUI / "tempos.json").read_text(encoding="utf-8"))
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    linhas = []
    for c in cenas:
        if c["inicio_capitulo"]:
            t = 0 if c["id"] == "001" else tempos["cenas"][c["id"]]
            linhas.append(f"{mmss(t)} {CAPITULOS[c['capitulo']]}")
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{LICENCA}\n\n{FONTES}\n\n{MUSICA}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / "descricao.md").write_text(texto, encoding="utf-8")
    print(len(texto), "caracteres")


if __name__ == "__main__":
    main()
