# everything defined outside classes and functions
# at zero indentation level are global = visible everywhere
# use as little globals as possible
x = 5

def f1():
    # this x is referring to global x, because the local name space has no x
    print(x)

def f2():
    global x
    x = x+1 # this will increase global x by 1
    print(x)
    
def f3():
    y = 2 # this is a local variable, no local keyword needed, because there
    # is no global variable of same name
    print(y)
    
def f4(x):
    # this x is once again local, because parameters are local.
    # global x doesn't matter!
    print(x)

f1()
f2()
f3()
f4(4)

