# Example of loop using tail recursion
def f(n):
    print(n)
    if n > 0:
        f(n-1)

f(10)  # print from 10 to 0

def factorial(n):
    if n == 0: return 1
    if n > 0: return n*factorial(n-1)

print(factorial(6))  # 6*5*4*3*2*1 = 720
