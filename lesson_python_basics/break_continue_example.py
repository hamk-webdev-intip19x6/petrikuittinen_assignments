while True:
    s = input("positive integer?")
    if not s.isdigit():
        continue  # go to beginning
    i = int(s)
    if i > 0:
        break
