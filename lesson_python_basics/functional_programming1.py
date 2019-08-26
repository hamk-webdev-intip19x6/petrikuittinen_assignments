# in Python 2 reduce in built-in function
# in Python 3 you must import reduce from functools
from functools import reduce
a = list(range(1, 11))
b = list(map(lambda x: x*x, a)) # square items
c = list(filter(lambda x: x%2==0, a)) # select even
d = reduce(lambda x, y: x+y, a) # calculate sum
print(a,b,c,d)
# chain b, c,d
e = reduce(lambda x, y: x+y, map(lambda x: x*x, filter(lambda x: x%2==0, a)))
print(e)
# same with list comprehension
sum([x*x for x in a if x%2==0])
