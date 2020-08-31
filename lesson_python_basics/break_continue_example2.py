numbers = []
while True:
    s = input("positive integer?")
    if not s: # almost same as if len(s) == 0:
        break
    if not s.isdigit():
        continue  # go to beginning
    i = int(s)
    if i >= 0:
        numbers.append(i)
print("Numbers", numbers)
print("Sum:", sum(numbers))
