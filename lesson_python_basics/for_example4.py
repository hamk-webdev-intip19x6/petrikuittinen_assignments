# range(begin, end, step)

names = ["Jack", "Bob", "Bill", "Alice", "Jane", "Liza"]

# this will create a new list which is reversed, slow if list is huge
for name in names[::-1]:
    print(name)
# more efficient way to iterate a sequence in reverse order    
print("Faster and more readable:")
for name in reversed(names):
    print(name)
    
    
