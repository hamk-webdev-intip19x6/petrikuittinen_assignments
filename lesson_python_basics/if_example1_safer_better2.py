while True:
    try:
        age = float(input("How old are you?"))
        break
    except ValueError:
        print("You didn't give me a number")

# age >=0 && age < 18
if 0<=age<18:
    print("You are still classfied as a child")
elif age>=18:
    print("You are classified as an adult")
    