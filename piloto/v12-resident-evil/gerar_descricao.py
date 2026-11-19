"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v12-resident-evil/gerar_descricao.py        # tempos.json -> descricao.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca; capítulos começam em 0:00, são 3 ou mais e duram
10 s ou mais; limite de 5000 caracteres.
"""

import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "One night left", "1": "9:40 PM: the first alert", "2": "10:30 PM: leaving", "3": "11:15 PM: the highway",
    "4": "Midnight: the tunnel", "5": "1:00 AM: Umbrella", "6": "2:00 AM: the line", "7": "2:30 AM: the helicopter",
    "8": "4:00 AM: the mountains", "9": "Dawn", "10": "Sunrise",
}

TOPO = """Could you escape Raccoon City as an ordinary resident on the night of the new Resident Evil (2026)? We live that night hour by hour, from the first "riot" alert to the mountains at dawn.

The film, the games and real history are kept separate: the night and the city come from Zach Cregger's film, what the authorities do comes from the games, and how people really behave comes from real disasters: the Sverdlovsk anthrax leak, Hurricane Rita, the 9/11 evacuation, the Ebola quarantine of West Point.

An independent, fan-made look at the story. Not affiliated with Capcom, Sony Pictures, Constantin Film or PlayStation Productions."""

FONTES = """SOURCES
- Meselson et al., "The Sverdlovsk anthrax outbreak of 1979", Science 266 (1994)
- NIST NCSTAR 1-7, Occupant Behavior, Egress, and Emergency Communications (World Trade Center, 2005)
- E. L. Quarantelli, "The Sociology of Panic", Disaster Research Center, Preliminary Paper 283 (2001)
- Nextgov: FCC and DHS on the 2011 Virginia earthquake and wireless 911 congestion (Aug 24 and Nov 28, 2011)
- NOAA National Hurricane Center, Tropical Cyclone Report: Hurricane Rita (2006)
- Texas House Research Organization, "Evacuation Planning in Texas", Interim News 79-2 (2006)
- World Health Organization, Rabies fact sheet (2026)
- Time and NPR on the West Point quarantine, Monrovia, August 2014
- Apple Support, "If your iPhone or iPad gets too hot or too cold"
- Kotaku (July 24, 2026) and PlayStation Blog (April 30, 2026) interviews with Zach Cregger
- Resident Evil (2026), dir. Zach Cregger; Resident Evil 2 and 3 (Capcom) for the game lore

Film and game details are marked as such in the narration. Real-world facts come from the sources above.
Illustrations: AI-generated in a custom style. Narration: synthetic voice."""

MUSICA = """MUSIC
"Night on the Docks - Sax" by Kevin MacLeod (incompetech.com), licensed under CC BY 3.0 (creativecommons.org/licenses/by/3.0)
"Dark Ambient - Horror Background Music No Copyright" by THRLL, https://www.youtube.com/watch?v=oO0DvpIWhd0
Music provided by Millennials Melody Originals. Free Download: https://melodly.net"""

HASHTAGS = "#ResidentEvil #RaccoonCity #ZachCregger"


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
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{FONTES}\n\n{MUSICA}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / "descricao.md").write_text(texto, encoding="utf-8")
    print(len(texto), "caracteres")


if __name__ == "__main__":
    main()
