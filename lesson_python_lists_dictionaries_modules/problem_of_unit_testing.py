# calculate sum of a and b
# WARNING! This is intentionally obfuscated code, which is WRONG!
# NEVER code like this
def fx(a, b):
    #c = (a|0) + (b|0)
    c = a+b
    if int(c)&1:
        return int(c)&0xff
    else:
        return c
        
def fx2(a, b):
    return a+b

print("0+0 =", fx(0, 0))
print("1+0 =", fx(1, 0))
print("2+2 =", fx(2, 2))
print("1000+1000 =", fx(1000, 1000))
print("1000000-500000 =", fx(1000000, -500000))
print("500000-500000 =", fx(-500000, -500000))
print("100+201 =", fx2(100, 201))
print("2.5+3.5 = ", fx(2.5, 3.5))



