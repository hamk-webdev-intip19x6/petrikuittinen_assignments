# WARNING! This program will fail on numeric input or with empty input
age = float(input("How old are you?"))
if age<0:
    print("Nobody can be so young.")
elif age<10:
    print("You are still young.")
else:
    print("You old fart.")
    

