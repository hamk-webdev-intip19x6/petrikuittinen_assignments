from timeit import Timer
# manually construct a list of squares
print(Timer('a=[];\nfor x in range(1,100001): a.append(x*x)').timeit(number=5))
# use list comprehension
print(Timer('[x*x for x in range(1,100001)]').timeit(number=5))
# use generators
print(Timer('list(x*x for x in range(1,100001))').timeit(number=5))
# Multiply x by 32
print(Timer('x=13;x*32').timeit())
# Shift x 5 bits left, same as *32
print(Timer('x=13;x<<5').timeit())
