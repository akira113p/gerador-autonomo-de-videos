"""Sobe um vídeo para o YouTube pela Data API v3. SEMPRE como privado: quem publica é você, no Studio.
Roda num venv só para isso (C:/ai-local/venv-yt) e usa credenciais que ficam fora do git (ferramentas/.youtube/).

  # uma vez: autorizar (abre o navegador; o token fica em ferramentas/.youtube/token.json)
  C:/ai-local/venv-yt/Scripts/python.exe ferramentas/youtube_upload.py --autorizar

  # subir: com publicacao.json na pasta do episódio, basta a pasta (título, tags, vídeo, thumb e legenda vêm dele)
  C:/ai-local/venv-yt/Scripts/python.exe ferramentas/youtube_upload.py piloto/v2-dia-em-roma

  # sem publicacao.json, tudo pela linha de comando
  C:/ai-local/venv-yt/Scripts/python.exe ferramentas/youtube_upload.py piloto/v2-dia-em-roma \\
      --video video_v2_jazz.mp4 --thumb thumb/thumb_3.jpg --titulo "What Did Ancient Romans Actually Do All Day?"

Cota: cada upload gasta ~1600 das 10.000 unidades diárias do projeto. Projeto de API não auditado: o YouTube trava
os vídeos enviados como privados (a publicação é manual no Studio, o que casa com "sempre assisto antes de publicar").
"""

import argparse
import json
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

AQUI = Path(__file__).resolve().parent
PASTA = AQUI / ".youtube"
CLIENT = PASTA / "client_secret.json"
TOKEN = PASTA / "token.json"
# upload + thumbnail + legenda; nada de ler ou apagar vídeos de outros
ESCOPOS = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.force-ssl"]
CATEGORIA_EDUCACAO = "27"


def credenciais(autorizar: bool = False) -> Credentials:
    cred = Credentials.from_authorized_user_file(TOKEN, ESCOPOS) if TOKEN.exists() else None
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
    elif not cred or not cred.valid:
        if not autorizar:
            sys.exit("sem autorização: rode com --autorizar primeiro")
        if not CLIENT.exists():
            sys.exit(f"falta {CLIENT} (baixe o JSON do cliente OAuth 'App para computador' no Google Cloud)")
        cred = InstalledAppFlow.from_client_secrets_file(str(CLIENT), ESCOPOS).run_local_server(port=0)
    TOKEN.write_text(cred.to_json(), encoding="utf-8")
    return cred


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta", nargs="?", help="pasta do episódio (tem o vídeo, a descrição e a legenda)")
    ap.add_argument("--autorizar", action="store_true")
    ap.add_argument("--video")
    ap.add_argument("--thumb")
    ap.add_argument("--titulo")
    ap.add_argument("--descricao", default="descricao.md")
    ap.add_argument("--legenda", default="legendas_en.srt")
    ap.add_argument("--tags", default="ancient rome,roman empire,history,daily life,martial,pompeii")
    ap.add_argument("--agendar", help="data/hora UTC ISO, ex.: 2026-10-17T19:00:00Z (continua privado até lá)")
    args = ap.parse_args()
    # publicacao.json da pasta do episódio preenche o que não veio na linha de comando
    pacote_path = Path(args.pasta) / "publicacao.json" if args.pasta else None
    if pacote_path and pacote_path.exists():
        pacote = json.loads(pacote_path.read_text(encoding="utf-8"))
        args.video = args.video or pacote.get("video")
        args.thumb = args.thumb or pacote.get("thumb")
        args.titulo = args.titulo or pacote.get("titulo")
        args.descricao = pacote.get("descricao", args.descricao)
        args.legenda = pacote.get("legenda", args.legenda)
        if pacote.get("tags"):
            args.tags = ",".join(pacote["tags"])

    PASTA.mkdir(exist_ok=True)
    cred = credenciais(args.autorizar)
    if args.autorizar and not args.pasta:
        print("autorizado")
        return
    if not (args.pasta and args.video and args.titulo):
        sys.exit("informe a pasta, --video e --titulo")

    pasta = Path(args.pasta)
    yt = build("youtube", "v3", credentials=cred)
    # "Conteúdo alterado ou sintético" (voz de IA) é uma pergunta do Studio: responda lá antes de publicar
    status = {"privacyStatus": "private", "selfDeclaredMadeForKids": False}
    if args.agendar:
        status["publishAt"] = args.agendar
    corpo = {"snippet": {"title": args.titulo, "description": (pasta / args.descricao).read_text(encoding="utf-8"),
                         "tags": args.tags.split(","), "categoryId": CATEGORIA_EDUCACAO,
                         "defaultLanguage": "en", "defaultAudioLanguage": "en"},
             "status": status}
    req = yt.videos().insert(part="snippet,status", body=corpo,
                             media_body=MediaFileUpload(str(pasta / args.video), chunksize=8 * 1024 * 1024,
                                                        resumable=True))
    resp = None
    while resp is None:
        prog, resp = req.next_chunk()
        if prog:
            print(f"enviado {prog.progress():.0%}", flush=True)
    vid = resp["id"]
    print("vídeo (privado):", f"https://studio.youtube.com/video/{vid}/edit")

    if args.thumb:
        yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(str(pasta / args.thumb))).execute()
        print("thumbnail ok")
    if (pasta / args.legenda).exists():
        yt.captions().insert(part="snippet", body={"snippet": {"videoId": vid, "language": "en", "name": "English"}},
                             media_body=MediaFileUpload(str(pasta / args.legenda))).execute()
        print("legenda ok")


if __name__ == "__main__":
    main()
