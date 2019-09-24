d = {"cat": "kissa"}
while True:
    word = input("Search for word or press just enter to QUIT?")
    word = word.strip().lower()
    if not word: break
    if word in d:
        print(word, "=", d[word])
    else:
        definition = input(word+" not found. Give definition for it or press enter to CANCEL?")
        if definition:
            d[word] = definition

            
