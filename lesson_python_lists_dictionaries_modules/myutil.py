"""Miscellaneous utility functions
Made by Petri Kuittinen 2017
"""
def askFloat(question):
    """display the question string and wait for standard input
    keep asking the question until user provides a valid floating point number
    return the number
    """
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("You didn't give me a number")

def lbsToKg(lbs):
    """Convert pounds (lbs) to kilograms (kg)
    """
    return lbs*0.45359237

def main():
    """Main program to test the module"""
    print(lbsToKg(askFloat("Give me pounds?")))

#main()
if __name__ == "__main__":
    main()
    
