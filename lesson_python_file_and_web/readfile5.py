with open("test.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        print(i, line.rstrip())
