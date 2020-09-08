def f1(x):
    y = x*7
    return y

def f2(x):
    global y
    y = x*2
    return y

def f3(x):
    return y*3

f3(3); f2(2); f1(1); print(y)
x = f1(1);x = f2(2); x = f3(3); print(y)

