#!/usr/bin/python3

# implement loop using tail recursion
def loop(x):
    print(x)
    if (x<100): loop(x+1)
loop(1)

