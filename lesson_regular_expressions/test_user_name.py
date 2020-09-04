import re
def valid_user_name(s):
    return re.fullmatch(r"[a-z][a-z\d]{2,9}", s)

user_name = input("user name?")
# use regular expression to test that user_name
# begins with character a-z and has 3 to 10 characters in length
# and only contains characters a-z 0-9
if valid_user_name(user_name):
    print("User name ok")
else:
    print("Invalid user name")

