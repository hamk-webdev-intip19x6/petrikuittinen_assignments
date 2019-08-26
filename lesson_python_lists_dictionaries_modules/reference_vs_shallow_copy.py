a = [1, 2, -4, 100]
b = a # b is now reference to a, not a copy!
b[0] = "flower"
print(b)
print(a) # both are changed, because they point to same memory location

# solution to this problem
print("Do like this instead:")
a = [1, 2, -4, 100]
b = a[:] # b is now a shallow copy of a
b[0] = "flower"
print(b) # 'flower' here
print(a) # no 'flower' here
