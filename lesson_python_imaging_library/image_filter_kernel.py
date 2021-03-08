#!/usr/bin/python3

from PIL import Image, ImageFilter
# kernel = ImageFilter.Kernel((3, 3), [1, 2, 1, 2, 4, 2, 1, 2, 1], 16) # gaussian blur
#kernel = ImageFilter.Kernel((3, 3), [1, 1, 1, 1, 1, 1, 1, 1, 1], 9) # blur
#kernel = ImageFilter.Kernel((3, 3), [0, 1, 0, 1, -4, 1, 0, 1, 0], 1) # find edges
kernel = ImageFilter.Kernel((3, 3), [-2, -1, 0, -1, 1, 1, 0, 1, 2], 1) # emboss
im = Image.open("../assets/bridge_in_rome.jpg")
im2 = im.filter(kernel)
im2.save("bridge_in_rome_filtered.jpg")
