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

def lbsTokg(lbs):
    """Convert pounds (lbs) to kilograms (kg)
    """
    return lbs*0.45359237

lbs = askFloat("How many pounds (lbs) ?")
print("%.2f kg" % lbsTokg(lbs)) 
