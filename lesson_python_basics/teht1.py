d = {"cat": "kissa", "dog": "koira"}
while True:
    word = input("Give me a word?")
    if not word: break
    if word in d:
        print(d[word])
    else:
        definition = input("Word not found. Give me definition or enter to cancel?")
        if definition:
            d[word] = definition
