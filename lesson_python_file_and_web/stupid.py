# Let's first define a list of numbers
a = [1, 2, 3, 10, -5]

# STUPID Python code

i = len(a)
sumx = 0
while i>0:
    i -= 1
    print(a[i])
    sumx += a[i]
print("sum ", sumx)

# BETTER way of doing the same in Python
for i in reversed(a):
    print(i)
print("sum", sum(a))
