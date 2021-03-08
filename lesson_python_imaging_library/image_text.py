#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw

im = Image.open("../assets/bridge_in_rome.jpg")
draw = ImageDraw.Draw(im)
# use a truetype font
font = ImageFont.truetype("../assets/Roboto-Regular.ttf", 40)
draw.text((50, 25), "Photo by Petri Kuittinen", font=font, fill=(150,0,0))
im.save("bridge_in_rome_text.jpg")
