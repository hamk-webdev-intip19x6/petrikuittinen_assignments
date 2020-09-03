f = open("test.txt", "r")  # open file in read (text) mode, which is default
data = f.read()
print(data, end="")
f.close()
