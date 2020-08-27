s = "this is easy"
n = len(s) # n = 12
print(s.count("i")) # how many "i":s
words = s.split()
sentence = " ".join(words)
print(words, sentence)
if words == sentence:
    print("equal")
a = []
a.append(1)
a.append(2)
a.append(100) 
print(a[1])  # print second item
print(a.pop())  # print last item and remove it
print(a.pop(0))  # print first item and remove it
a.insert(1,"second")  # insert to specified location
