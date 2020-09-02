f = lambda x: x+1
# same written as function, using def
def f(x):
    return x+1

print(f(5))  # 6


product = lambda a, b: a*b
print(product(3, 2))  # 6

my_abs = lambda x: x if x >= 0 else -x
print(my_abs(-5))  # 5
