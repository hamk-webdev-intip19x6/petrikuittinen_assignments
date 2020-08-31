import time

a = list(range(10**7))

def time_func(func):
    time1 = time.time()
    func()
    time2 = time.time()
    return time2-time1

def normal_order():
    for x in a:
        pass

def reverse_order():
    for x in reversed(a):
        pass

def reverse_slicing():
    for x in a[::-1]:
        pass

def reverse_while():
    i = len(a)-1
    while i >= 0:
        x= a[i]
        i = i-1

def reverse_range():
    for x in range(len(a)-1, -1, -1):
        pass

print("Normal order:")
print(time_func(normal_order))

print("Reversed order:")
print(time_func(reverse_order))

print("Reverse slicing:")
print(time_func(reverse_slicing))

print("Reverse while:")
print(time_func(reverse_while))

print("Reverse range:")
print(time_func(reverse_range))

