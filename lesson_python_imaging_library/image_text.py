#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw

im = Image.open("../assets/fitness.jpg")
draw = ImageDraw.Draw(im)
# use a truetype font
font = ImageFont.truetype("../assets/Roboto-Regular.ttf", 40)
draw.text((50, 25), "Petri Kuittinen", font=font, fill=(255,0,0))
im.save("fitness_text.jpg")

