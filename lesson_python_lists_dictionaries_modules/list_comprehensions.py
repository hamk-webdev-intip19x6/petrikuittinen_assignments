# many ways to define lists
a = list(range(1, 101)) # type cast range iterator into a list
print(a)
a = [i*i for i in range(1, 101)]
print(a)
a = [i*i for i in range(1, 101) if i%2]
print(a)
