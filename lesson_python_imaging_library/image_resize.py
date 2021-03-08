#!/usr/bin/python3
# resize image while retaining aspect ratio
from PIL import Image
im = Image.open("../assets/bridge_in_rome.jpg")
width, height = im.size
ratio = width/height
new_width = 640
new_height = new_width/ratio
im2 = im.resize((round(new_width), round(new_height)), Image.ANTIALIAS)
im2.save("bridge_in_rome2.jpg", quality=90, optimize=True)

