x = 2  # global x


def f(x):  # this parameter x is local
    x = x * 2  # this is local x
    y = x * 2  # this is local y
    return y


print("x =", x)
y = f(3)  # this is global y
print("y =", y)
print("x =", x)
x = 10  # this is global x
print("x =", x)
