# A function returning a function
def make_adder(n):
    def adder(x):
        return x+n
    return adder

# More concise version
def make_adder(n):
    return lambda x: x+n

inc2 = make_adder(2)
print(inc2(4))
