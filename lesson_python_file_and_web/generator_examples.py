def reverse(data):
    """Generator iterating backwards"""
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('spam'):
    print(char)
    
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

f = fib()
for x in range(2000):
    print(next(f))

