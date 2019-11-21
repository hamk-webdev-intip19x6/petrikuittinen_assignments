from random import choice
import string
chars = string.ascii_letters+string.digits
n = int(input("How many characters?"))
for i in range(n):
    print(choice(chars), end='')
print()
