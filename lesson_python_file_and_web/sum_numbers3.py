path = input("Give me file path?")
sumx = 0
try:
    with open(path) as f:
        for line in f:
            try:
                n = float(line.rstrip())
                sumx += n
            except ValueError:
                pass
        print("sum =", sumx)
except OSError as err:
    print("Error:", err)

