"""modulin documentation string tulisi tähän"""

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

age = askFloat("How old are you?")
if age<0:
    print("Nobody can be that young")
elif age<10:
    print("You are still a child")
else:
    print("You old fart")
    