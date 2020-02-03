names = ["Bill", "James", "Paul", "Paula", "Jenny", "Kate"]
# normal order
for name in names:
    print(name)

print("Reverse order:")
for name in reversed(names):
    print(name)
    
print("Don't code like this")
i = len(names)-1
while i >= 0:
    print(names[i])
    i = i-1
