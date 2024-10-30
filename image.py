from PIL import Image, ImageDraw, ImageFont

def createTicket(name, nationality, order, filename):
    img = Image.open("./static/template.png")
    order = str(order)
    order1 = order
    for x in range(6 - len(order)):
        order = "0"+ order
    d = ImageDraw.Draw(img)
    fontsize = 50
    font = ImageFont.truetype("Myriad Pro Regular.ttf", fontsize)
    d.text((560,257), name, font=font, fill=(227,69,69))
    d.text((1170,257), nationality, font=font, fill=(227,69,69))
    d.text((1620,130), order, font=font, fill=(255,255,255))
    # d.text((1600,270), name, font=font, fill=(0,0,0))
  
    txt=Image.new('L', (500,50))
    textName = ImageDraw.Draw(txt)
    textName.text( (0, 0), name,  font=font, fill=(255))
    w=txt.rotate(-90,  expand=1)
    # img.paste( ImageOps.colorize(w, (200,0,0), (0,0,0)), (1865,100),  w)
    img.paste((255,255,255), box=(1855,100), mask=w) 

    txt=Image.new('L', (500,50))
    textorder = ImageDraw.Draw(txt)
    textorder.text( (0, 0), order,  font=font, fill=255)
    w=txt.rotate(-90,  expand=1)
    # img.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (1865,585),  w)
    img.paste((255,255,255), box=(1855,585), mask=w) 
        
    img.save("static/images/" + filename + ".png")
    return filename + ".png"

# sys.modules[__name__] = createTicket
