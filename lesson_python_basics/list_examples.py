s = "this is easy"
n = len(s) # n
words = s.split()
sentence = " ".join(words) # form back the sentence
if words == sentence:
    print("equal")
print("backwards", s[::-1])
a = list(range(1,11))
print(sum(a)) # 55
from random import shuffle
shuffle(a)
a.sort()
a.reverse()
a.sort(reverse=True) # more efficient way
