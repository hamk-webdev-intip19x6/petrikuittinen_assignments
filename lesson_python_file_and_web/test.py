def f1(x):
    y = x*7
    return y
def f2(x):
    global y
    y = x*2
    return y
def f3(x):
    return y*3

#After the above function definitions the following code will fail on error:
#f3(3)
#f2(2)
#f1(1)
#print(y)
#After the above code, the following will print out 4:

x = f1(1)
x = f2(2)
x = f3(3)
print(y)