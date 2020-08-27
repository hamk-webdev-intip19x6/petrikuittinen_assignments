from collections import deque
from timeit import timeit

def list_test(n):
    a = []
    for i in range(n):
        a.insert(0, i)
    return a

def deque_test(n):
    a = deque([])
    for i in range(n):
        a.insert(0, i)
    return a

if __name__ == '__main__':
    print("List:", timeit('list_test(10**5)', setup='from __main__ import list_test', number=10))
    print("Deque:", timeit('deque_test(10**5)', setup='from __main__ import deque_test', number=10))

