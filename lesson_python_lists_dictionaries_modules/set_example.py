a = {1, 2, 3, 4, 5}
b = {10, 8, 7, 5, 4}
c = a.union(b)
d = set([7, 5])
print("length", len(a))
if 3 in a:
    print("3 found in a")
print("union", c)
if a.issubset(c):
    print("a is subset of c")
print("intersection", a.intersection(b))
print("difference", a.difference(b))
print("symmetric difference", a.symmetric_difference(b))
readonly = frozenset([1, 2, 3])
