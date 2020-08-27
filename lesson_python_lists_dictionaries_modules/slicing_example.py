s = "abc123"
print(s[2:])    # omit first 2 characters "c123"
print(s[-1])    # last character "3"
print(s[:-3])   # omit last 3, "abc"
print(s[2:5])   # "c12"
print(s[::2])   # every second character "ac2"
print(s[::-1])  # reverse "321cba"
a = ["one", "two", "three", "four"]
print(a[-2])    # second last, "three"
print(a[::-1])  # ['four', 'three', 'two', 'one'] 
a[1:3] = ["kaksi", "kolme"]
print(a)        # ['one', 'kaksi', 'kolme', 'four']
