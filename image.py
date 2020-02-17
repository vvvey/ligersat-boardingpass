from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys

# listofname = ["Vuthy vey", "Reaksmy Dancer", "Visal Sao", "mengthong LONg","រំដួល"]
# # img = Image.new('RGB', (100, 30), color = (73, 109, 137))
def createTicket(name, nationality, id):
    img = Image.open("test.png")
    id = str(   id)
    for x in range(6 - len(id)):
        id = "0"+ id
    d = ImageDraw.Draw(img)
    fontsize = 50
    font = ImageFont.truetype("Myriad Pro Regular.ttf", fontsize)
    d.text((545,270), name, font=font, fill=(0,0,0))
    d.text((1090,270), nationality, font=font, fill=(0,0,0))
    d.text((1570,130), id, font=font, fill=(0,0,0))
    # d.text((1600,270), name, font=font, fill=(0,0,0))
    
    txt=Image.new('L', (500,50))
    textName = ImageDraw.Draw(txt)
    textName.text( (0, 0), name,  font=font, fill=255)
    w=txt.rotate(-90,  expand=1)
    img.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (1865,100),  w)
    
    txt=Image.new('L', (500,50))
    textID = ImageDraw.Draw(txt)
    textID.text( (0, 0), id,  font=font, fill=255)
    w=txt.rotate(-90,  expand=1)
    img.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (1865,585),  w)
    
    img.save("static/" + name + ".png")
    return name + ".png"

sys.modules[__name__] = createTicket

