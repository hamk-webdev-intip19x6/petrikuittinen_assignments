# * before argument will return a tuple of 0..N arguments
def mysum(*n):
    total = 0
    for i in n:
        total += i
    return total

print(mysum(1, 2, 10))
# sum([1, 2, 10]) would do the same

# ** before argument will return a dictionary of 0..N keyword arguments
def login(**parameters):
    if "user" in parameters:
        print("User name:", parameters.get("user"))
    if "password" in parameters:
        print("Password:", parameters.get("password"))

login(user="root", password="qwerty")
# Note that the following will fail, because it has
# no keyword arguments
# login("root", "qwerty")
