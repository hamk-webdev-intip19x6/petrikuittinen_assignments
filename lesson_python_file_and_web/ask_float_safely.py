def ask_float(question):
    """display the question string and wait for standard input
    keep asking the question until user provides a valid floating
    point number. Return the number"""
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Please give a valid floating point number")


def lbs_to_kg(lbs):
    """Convert pounds (lbs) to kilograms (kg)"""
    return lbs * 0.45359237


lbs = ask_float("How many pounds (lbs) ?")
print(f"{lbs_to_kg(lbs):.2f} kg")
