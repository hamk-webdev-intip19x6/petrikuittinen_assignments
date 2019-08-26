#!/usr/bin/python3

from PIL import Image, ImageEnhance
im = Image.open("../assets/fitness.jpg")
enhancer = ImageEnhance.Color(im) 
im2 = enhancer.enhance(0) # turn into black & white
im2.save("fitness_enhanced.jpg") 

