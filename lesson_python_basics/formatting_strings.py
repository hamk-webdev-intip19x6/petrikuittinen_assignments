import math

print("%.2f" % math.pi) # display with 2 digit precision
name = "Jack"
age = 25

print("My name is %(name)s. And %(name)s's age is %(age)d." % {"name": name, "age": age})
# the lazy solution
print("My name is %(name)s. And my age is %(age)d." % vars())


    