import mypackage.mymath
import re

s = input("Give me numbers separated by comma?")
try:
    numbers = [float(x) for x in re.split(r",\s*", s)]
    print("Average:", mypackage.mymath.average(numbers))
except ValueError:
    print("Invalid input.")
