x = [1, 2, 3]
y = ['a', 'b', 'c']
z = list(zip(x, y))
# z is now basically a 2-dimensional struct: several tuples inside a list
print(z)
# iterate using stupid way
for t in z:
    print (t[0], t[1])
# using automatic unpacking
for i, j in z:
    print(i, j)
