#!/usr/bin/python3

from PIL import Image, ImageFilter
im = Image.open("../assets/fitness.jpg")
im2 = im.filter(ImageFilter.FIND_EDGES)
#im2 = im.filter(ImageFilter.BLUR)
#im2 = im.filter(ImageFilter.DETAIL)
#im2 = im.filter(ImageFilter.SHARPEN)
im2.save("fitness2.jpg")

