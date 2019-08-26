s = "program"
print(len(s)) # length of string/sequence, 7
# indexing strings or any other sequence type
# indexes start from 0
# negative index -1 starts from the ned
# [begin:end:step]
# if one part is missing assume 0 for begin, length for end and 1 for step
print(s[0]) # first character of string, p
print(s[1]) # second character of string, r
print(s[-1]) # last character of string, m
print(s[-2]) # second last character of string, a
print(s[0:3]) # "pro"
print(s[1:4]) # "rog"
print(s[::2]) # "porm"
print(s[::-1]) # reversed "margorp"

