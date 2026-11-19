import sys
from pathlib import Path
from PIL import Image, ImageDraw
A=Path(__file__).resolve().parent
ini,fim=int(sys.argv[1]),int(sys.argv[2])
fs=[f for f in sorted((A/"imagens").glob("*.png")) if ini<=int(f.stem[:3])<=fim]
cols=4; w,h=480,270; rows=(len(fs)+cols-1)//cols
c=Image.new("RGB",(w*cols,h*rows))
for i,f in enumerate(fs):
    im=Image.open(f).resize((w,h)); ImageDraw.Draw(im).text((6,4),f.stem,fill=(255,255,0))
    c.paste(im,(w*(i%cols),h*(i//cols)))
c.save(A/"folha.png"); print(len(fs))
