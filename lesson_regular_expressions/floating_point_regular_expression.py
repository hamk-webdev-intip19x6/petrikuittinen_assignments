import re

re_floating_number = re.compile(r"[-+]?\d*\.?\d+")
re_floating_exponent = re.compile(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')

s = "Here are some floating point numbers: 3.14 123.45678, 0.2:0.0 -5.6 +3.54, 0.0001 10.0 and -2.0"

num_strings = re_floating_number.findall(s)
print(num_strings)
