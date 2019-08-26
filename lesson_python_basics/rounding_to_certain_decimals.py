# printing numbers with certain amount of decimals
x = 123.45678585
print("2 desimaalin tarkkuudella %.2f ja kolmen %.3f ." % (x, x))

age = 15
name = "Jack"
print("My name is %(name)s and my age is %(age)d." % {"age": age, "name": name})
# or if you are lazy, like your teacher, you can write:
print("My name is %(name)s and my age is %(age)d." % vars())

