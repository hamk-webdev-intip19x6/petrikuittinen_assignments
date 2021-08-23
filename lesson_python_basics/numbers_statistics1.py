numbers = []
while True:
    s = input("Give me a number (enter to stop)?")
    if not s: break
    try:
        n = float(s)
        numbers.append(n)
    except ValueError:
        print("Invalid number. Please give me valid floating point numbers.")

print(f"Number of numbers: {len(numbers)}")
print("Numbers sorted:")
for i in sorted(numbers):
    print(i)
    