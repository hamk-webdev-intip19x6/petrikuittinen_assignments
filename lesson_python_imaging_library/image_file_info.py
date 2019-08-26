#!/usr/bin/python3

from PIL import Image
im = Image.open("../assets/fitness.jpg")
#im = Image.open("../assets/sprites.png")
print("Image format:", im.format)
print("Mode:", im.mode)
print("Dimensions", im.size) # width, height tuple


