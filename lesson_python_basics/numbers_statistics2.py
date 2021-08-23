
def average(a):
    """Return arithmetic mean of list of floating point numbers"""
    return sum(a)/len(a)

def main():
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
    print(f"Average: {average(numbers)}")
    print("Numbers sorted:")
    for i in sorted(numbers):
        print(i)

if __name__ == "__main__":
    main()
