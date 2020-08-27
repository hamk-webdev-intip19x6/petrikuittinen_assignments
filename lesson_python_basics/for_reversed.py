names = ["Bill", "James", "Paul", "Paula", "Jenny", "Kate"]

print("Normal order:")
for name in names:
    print(name)

print("Reverse order:")
for name in reversed(names):
    print(name)

print("This will also do the same, but less efficient:")
for name in names[::-1]:
    print(name)

print("Don't code like this:")
i = len(names)-1
while i >= 0:
    print(names[i])
    i = i-1

# this also works, but unreadable
for i in range(len(names)-1, -1, -1):
    print(names[i])