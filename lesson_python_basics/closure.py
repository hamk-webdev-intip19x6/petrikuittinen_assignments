# Example of a closure
def make_multiplier(x):  # outer / enclosing function
    def multiplier(y):  # inner / nested function
        return x*y
    return multiplier

mul10 = make_multiplier(10)  # mul is the closure function 
print(mul10(5))  # 50
print(mul10(10))  #100
mul2 = make_multiplier(2)
print(mul2(10))  # 20
