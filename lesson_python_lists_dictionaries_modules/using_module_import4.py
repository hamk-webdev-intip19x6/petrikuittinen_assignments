from myutil import askFloat as kysyLuku
# WARNING: Do NOT use this often, because local name space becomes polluted!
# if you import like this then the name is copied to the local name space
# and no prefix is required
x = kysyLuku("Give me a float?")
print(x)
