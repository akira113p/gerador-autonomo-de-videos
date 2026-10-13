"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v8-navio-viking/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v8-navio-viking/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: a land deal in Iceland",
    "1": "Meet Erik the Red",
    "2": "The ship you will really board",
    "3": "The warship, and how fast it was",
    "4": "Sailing without a compass",
    "5": "Food, sleep and seasickness",
    "6": "Fourteen out of twenty-five",
    "7": "Life in Greenland",
    "8": "Traders, not just raiders",
    "9": "Vinland and L'Anse aux Meadows",
    "10": "Viking myths: horns, skulls and the gods",
    "11": "Why the ship mattered",
}

TOPO = """What would your life be like on a Viking ship? Climb aboard with a farmer from Iceland in the year 985, who says yes to a very good deal from Erik the Red: free land in a place called Greenland.

The ship is not the one from the movies. We look at the cargo ship that really crossed the North Atlantic, how sailors found their way without a compass, what they ate and where they slept, the fleet where only 14 of 25 ships arrived, life in Greenland, the Vikings as traders, the sagas' Vinland, the real Viking site at L'Anse aux Meadows, and a few myths about horned helmets and skull cups."""

FONTES = """SOURCES
- The Saga of Erik the Red and the Saga of the Greenlanders (Icelandic sagas, written down in the 13th century)
- Landnámabók (Book of Settlements), sailing directions to Greenland
- Viking Ship Museum, Roskilde: Ottar (Skuldelev 1), the Sea Stallion from Glendalough (Skuldelev 2), "Sea fare and menu", and the Skjoldungen history pages
- Canadian Mysteries (University of Victoria): Eirik Thorvaldson, sailing directions and Vinland pages
- Ahmad ibn Fadlan, Risala (922), in James Montgomery's translation, Journal of Arabian and Islamic Studies
- The Gokstad ship and the 1893 replica voyage to Chicago
- NOVA/PBS, "Secrets of Viking Ships"
- Barrett et al., Greenland and the medieval walrus ivory trade (University of Cambridge)
- Kuitems et al., "Evidence for European presence in the Americas in AD 1021", Nature (2021)
- Ropars et al. (2011), Iceland spar and the Viking "sunstone"
- Britannica: the Lindisfarne raid of 793
- University of Nottingham: what the word "Viking" really meant
- Oxford University Press blog, "Ten myths about the Vikings"
- Manar Hammad (2023) on Arab silver coins in Viking Age Scandinavia
- Mail & Guardian (2007) on the Sea Stallion crossing to Dublin

Some details are reconstructed from general accounts, and the sagas disagree with each other in places. The farmer and his family are fictional.
Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#Vikings #History #VikingShip"


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
