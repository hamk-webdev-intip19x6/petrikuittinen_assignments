def f(n):
    print(n)
    if n>0: f(n-1)

f(10)

def fact(n):
    if n==0: return 1
    if n>0: return n*fact(n-1)

print(fact(6)) # 6*5*4*3*2*1 = 720

