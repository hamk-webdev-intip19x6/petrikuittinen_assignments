# python lists are mutable collections of data
# their size and content can change as much as you want within limits of memory
a = [] # empty list
a.append(1) # add to end of list
a.append(2)
print(a.pop()) # remove the last item and return it
print(a[0]) # indexes start from 0
a[0] = 100 # resign new value to a
print(a[0])
a.append("cat")
a.append("dog")
print(a)
a.reverse() # reverse order of items
print(a)
a.remove("cat") # remove first occurence of "cat"
a.remove("dog")
a.append(3)
a.append(-5)
print(a)
a.sort() # sort to ascending order
print(a)
b = [1, 2, 3, 1] # predefined list
print(len(b)) # length of list
print(b.count(1)) # count occurence of 1s in list
numbers = [0]*1000 # list of a thousand zeros
print(len(numbers))
