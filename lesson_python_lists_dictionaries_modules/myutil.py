"""Miscellaneous utility functions
Made by Petri Kuittinen 2017-2020
"""


def ask_float(question):
    """Display the question string and wait for standard input.
    Keep asking the question until user provides a valid floating point number.
    Return the number."""
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("You didn't give me a number")


def lbs_to_kg(lbs):
    """Convert pounds (lbs) to kilograms (kg)"""
    return lbs * 0.45359237


def main():
    """Main program to test the module"""
    print(lbs_to_kg(ask_float("Give me pounds?")))

if __name__ == "__main__":
    main()
