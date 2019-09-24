import re
s = input("Give me a string?")
print(" ".join(re.findall(r".{1,4}", s)))

