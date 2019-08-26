# Let's first define a list of numbers
a = [1, 2, 3, 10, -5]

# STUPID Python code
def mysum(a):
    sumx = 0
    for i in a:
        sumx += i
    return sumx
    
def average(a):
    return mysum(a)/len(a)
    
print("Average", average(a))

# BETTER way of doing the same in Python
from statistics import mean
print("Average", mean(a))
