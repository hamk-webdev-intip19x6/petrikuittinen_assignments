#!/usr/bin/python3

from PIL import Image, ImageFilter
im = Image.open("../assets/bridge_in_rome.jpg")
im2 = im.rotate(90, resample=Image.BICUBIC, expand=True)
im2.save("bridge_rotated.jpg")

