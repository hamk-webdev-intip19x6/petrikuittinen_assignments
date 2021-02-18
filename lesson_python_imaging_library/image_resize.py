#!/usr/bin/python3
# resize image while retaining aspect ratio
from PIL import Image
im = Image.open("../assets/fitness.jpg")
width, height = im.size
ratio = width/height
new_width = 640
new_height = new_width/ratio
im2 = im.resize((round(new_width), round(new_height)), Image.ANTIALIAS)
im2.save("fitness2.jpg", quality=95, optimize=True)



