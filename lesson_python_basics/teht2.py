import re
from statistics import mean, median
s = input("Give me numbers?")
number_strings = re.findall(r"-?\d+", s)
numbers = list(map(int, number_strings))
#numbers = [int(x) for x in number_strings]
print("sum", sum(numbers))
print("mean", mean(numbers))
print("median", median(numbers))
