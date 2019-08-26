while True:
    try:
        age = float(input("How old are you?"))
        break
    except ValueError:
        print("You didn't give me a number")

if age<0:
    print("Nobody can be that young")
elif age<10:
    print("You are still a child")
else:
    print("You old fart")
    