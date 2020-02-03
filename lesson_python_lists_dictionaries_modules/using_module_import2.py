from myutil import askFloat, lbsToKg
# NOTICE: no .py needed here, just the part before .py
# if you import like this then the name is copied to the local name space
# and no prefix is required
x = askFloat("Give me a float?")
print(lbsToKg(x))
