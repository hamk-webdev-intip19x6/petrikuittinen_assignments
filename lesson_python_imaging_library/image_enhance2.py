#!/usr/bin/python3

from PIL import Image, ImageEnhance
im = Image.open("../assets/bridge_in_rome.jpg")
enhancer = ImageEnhance.Contrast(im)
# im2 = enhancer.enhance(0.5) # low contrast
im2 = enhancer.enhance(1.5) # high contrast
enhancer = ImageEnhance.Color(im2)
#im2 = enhancer.enhance(0) # turn into black & white
im2 = enhancer.enhance(1.5) # 50 % more colorful
im2.save("bridge_in_rome_enhanced.jpg") 

