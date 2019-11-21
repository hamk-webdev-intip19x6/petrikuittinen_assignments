#!/usr/bin/python3

from PIL import Image
im = Image.open("../assets/fitness.jpg")
width, height = im.size
#im2 = im.resize((round(width/2), round(height/2)), Image.ANTIALIAS)
#im2 = im.resize((round(width*2), round(height*2)), Image.ANTIALIAS)
im2 = im.resize((800, 600), Image.ANTIALIAS)
im2.save("fitness2.jpg", quality=95, optimize=True)



