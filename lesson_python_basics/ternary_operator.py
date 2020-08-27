x = float(input("Give me number?"))
# ternary operator is nice for short ifs
abs_x = x if x >= 0 else -x
# same as:
if x <= 0:
    abs_x = x
else:
    abs_x = -x

# can also be used in functions and lambdas
def myabs(x):
    return x if x >= 0 else -x

print("Absolute value is", myabs(x))

