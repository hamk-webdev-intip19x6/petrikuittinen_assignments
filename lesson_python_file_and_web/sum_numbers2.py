path = input("Give me file path?")
sumx = 0
with open(path) as f:
    for line in f:
        try:
            n = float(line.rstrip())
            sumx += n
        except ValueError:
            pass
print("sum =", sumx)
