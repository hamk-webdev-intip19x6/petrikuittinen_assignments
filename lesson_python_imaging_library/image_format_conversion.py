#!/usr/bin/python3
# Convert image into different formats
from PIL import Image
im = Image.open("../assets/piechart.gif") # open a GIF file
im.save("piechart.png") # PNG supports both P and RGB mode
im2 = im.convert("RGB") # convert P mode image to RGB mode
im2.save("piechart.jpg", quality=90, optimize=True)

