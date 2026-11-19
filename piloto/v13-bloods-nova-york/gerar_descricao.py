"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v13-bloods-nova-york/gerar_descricao.py        # tempos.json -> descricao.md

O nome real da facção só aparece no título do vídeo (decisão do usuário); aqui as fontes vão sem citar o nome.
Limite de 5000 caracteres; capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais.
"""

import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "It started in a jail", "1": "June: the offer", "2": "July: getting in", "3": "September: obligations",
    "4": "November: who you know", "5": "March: the takedown", "6": "April: the offer", "7": "The rule",
    "8": "One year", "9": "The founder",
}

TOPO = """What would the first year of your life look like if a New York gang recruited you at eighteen? This is a composite built from federal court records, NYPD and city data, and decades of research on gangs, not the life of any one real person.

It is journalism. It does not teach, encourage or glorify anything: every claim about a crime is attributed to a court record or a study, and every act comes with its legal consequence."""

FONTES = """SOURCES
- U.S. Attorney's Office, Southern District of New York: sentencing release on the founder (April 14, 2003); indictments and sentencings in the 2018-2020 Manhattan racketeering case
- U.S. Attorney's Office, Western District of North Carolina, indictment release (May 18, 2017)
- NYC Department of Investigation / OIG-NYPD, "An Investigation into NYPD's Criminal Group Database" (April 2023)
- NYPD year-end crime statistics (January 2023, January 2024, January 2026)
- Weerman & Thornberry, European Journal of Criminology 12(1) (2015)
- Pyrooz & Sweeten, "Gang Membership Between Ages 5 and 17 Years in the United States", Journal of Adolescent Health (2015)
- Thornberry et al., Gangs and Delinquency in Developmental Perspective (2003), via University at Albany
- Melde, Diem & Drake, Journal of Contemporary Criminal Justice 28(4) (2012)
- Patton et al., "Internet banging", New Media & Society (2016)
- Papachristos, Wildeman & Roberto, Social Science & Medicine (2015); Papachristos, Braga & Hureau, Journal of Urban Health (2012)
- Pyrooz, Decker & Webb, Crime & Delinquency 60(4) (2014); University of Colorado on Pyrooz's Texas prison study (2020)
- 18 U.S.C. §§ 1961-1963 (RICO) and § 924(c)
- The New York Times (January 31, 2000; December 4, 2019)

Illustrations: AI-generated in a custom style. Narration: synthetic voice."""

MUSICA = """MUSIC
"Covert Affair" by Kevin MacLeod (incompetech.com), licensed under CC BY 3.0 (creativecommons.org/licenses/by/3.0)
Music: Suspenseful by #soundridemusic
Link to Video: https://youtu.be/8abBSm3LZcs
"Isolated" (via "Sad Piano Background Music", MrSnooze, https://www.youtube.com/watch?v=FubpHGB4iq0), Creative Commons as credited there"""

HASHTAGS = "#NewYork #TrueStory #Documentary"


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
