#!/usr/bin/python3

from PIL import Image, ImageFilter
im = Image.open("../assets/fitness.jpg")
im2 = im.rotate(45, resample=Image.BICUBIC, expand=True)
im2.save("fitness_rotated.jpg")




