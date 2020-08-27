words = input("Give me words separated by spaces, but not word NO?").split()
for word in words:
    if word.lower() == "no": break
    print(word)
else:
    print("That was nice!")
