def mysum(*n):
    total = 0
    for i in n:
        total += i
    return total

print(mysum(1, 2, 10))

def login(**parameters):
    if "user" in parameters:
        print("User name:", parameters.get("user"))
    if "password" in parameters:
        print("Password:", parameters.get("password"))

login(user="root", password="qwerty")
