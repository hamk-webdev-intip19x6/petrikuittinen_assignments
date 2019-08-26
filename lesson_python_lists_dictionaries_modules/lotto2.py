from random import shuffle
numbers = list(range(1, 41)) # create numbers 1...40
shuffle(numbers) # shuffle numbers to random order
row = numbers[:7] # take first 7
row.sort()
print(", ".join([str(x) for x in row]))

