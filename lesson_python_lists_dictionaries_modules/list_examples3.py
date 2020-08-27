from random import shuffle
a = list(range(1,11))  # a = [1, 2, 3…10]
print("Sum:", sum(a)) # 55
print("Smallest:", min(a))
print("Largest:", max(a))
shuffle(a)
print("Shuffled;", a)
a.sort()
print("Sorted:", a)
a.reverse()
print("Reversed", a)
a.sort(reverse=True)  # more efficient way to do reverse sort
