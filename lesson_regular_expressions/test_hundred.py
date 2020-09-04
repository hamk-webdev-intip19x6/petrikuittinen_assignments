import re

s = input("Give me an integer 1-100?")
if re.match(r"^(100|[1-9]\d?)$", s):
    print("Correct")
else:
    print("Incorrect")
