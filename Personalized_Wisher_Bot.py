from pywebio import *
from pywebio.input import FLOAT, file_upload,input, select, input_group
from pywebio.output import put_text,put_image, style
from PIL import Image, ImageDraw, ImageSequence,ImageFont
import io
import random
import numpy as np

def GIF_Genrator(GIF_PATH,IMAGE_PATH,data,themenum):
    gif = Image.open(GIF_PATH)
    image = Image.open(IMAGE_PATH).resize((280, 280)).convert("P")
    frames = [f.copy() for f in ImageSequence.Iterator(gif)]
    fontstl = random.choice(font_list)
    for i, frame in enumerate(frames):
        frame = frame.convert("RGBA")
        frame.paste(image,data[indtheme_list[themenum]]["pic"])
        frames[i] = frame
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("fonts/"+fontstl, data[indtheme_list[themenum]][fontstl][1])
        color=tuple(np.random.choice(range(256), size=3))
        draw.text(data[indtheme_list[themenum]][fontstl][0], "Dear "+info['name']+"\n\nClointFusion wishes you a happy "+info['event'], color, font=font,align="center")
    frames[0].save("Generated_Ind_GIFs/"+info['img']['filename'].split(".")[0]+str(themenum+1)+".gif", save_all=True, append_images=frames[1:])     
    put_image(open("Generated_Ind_GIFs/"+info['img']['filename'].split(".")[0]+str(themenum+1)+".gif",'rb').read(),width="",height="")


info = input_group("User info",[input("Enter your name ",name = "name"),
select('Which gift you want?', ['Independence Day', 'Dussehra'],name = "event"), 
file_upload("Select a image:", accept="image/*",name = "img")])

image = Image.open(io.BytesIO(bytearray(info['img']['content'])))
image.save('userpics/'+info['img']["filename"]) 
IMAGE_PATH = 'userpics/'+info['img']['filename']
put_text("5 GIFs are being generated...Please Wait").style("text-align: center; color:brown; font-size:30px ;font-weight: bold")

font_list = ["disney.ttf","dotted.ttf","netflix.ttf","agethsa.ttf","younglines.ttf","regular.ttf"]
indtheme_list = ["theme1","theme2","theme3","theme4","theme5"]
data= {
    "theme1" : {"name" : "theme1.gif", "pic" : (870,320), "disney.ttf": [(100,600),110],"dotted.ttf": [(50,620),50],"netflix.ttf": [(80,620),100],"agethsa.ttf": [(20,600),110],"younglines.ttf": [(80,620),150],"regular.ttf": [(50,600),72] },
    
    "theme2" : {"name" : "theme2.gif", "pic" : (438,414), "disney.ttf": [(65,750),60],"dotted.ttf": [(40,750),29],"netflix.ttf": [(35,750),60],"agethsa.ttf": [(30,750),58],"younglines.ttf": [(50,750),85],"regular.ttf": [(30,750),43] }, 

    "theme3" : {"name" : "theme3.gif", "pic" : (150,380), "disney.ttf": [(30,690),95],"dotted.ttf": [(30,750),43],"netflix.ttf": [(30,720),88],"agethsa.ttf": [(30,730),85],"younglines.ttf": [(30,710),125],"regular.ttf": [(30,720),63] },

    "theme4" : {"name" : "theme4.gif", "pic" : (1536,250),"disney.ttf": [(5,400),80],"dotted.ttf": [(10,500),35],"netflix.ttf": [(5,400),70],"agethsa.ttf": [(10,480),73],"younglines.ttf": [(5,400),109],"regular.ttf": [(10,450),50] },

    "theme5" : {"name" : "theme5.gif", "pic" : (686,280), "disney.ttf": [(30,550),96],"dotted.ttf": [(30,650),43],"netflix.ttf": [(50,600),88],"agethsa.ttf": [(30,600),86],"younglines.ttf": [(10,600),135],"regular.ttf": [(10,600),64] },
    }

for i in range(5):
    GIF_PATH = "Independence-day/"+indtheme_list[i]+".gif"
    GIF_Genrator(GIF_PATH,IMAGE_PATH,data,i)