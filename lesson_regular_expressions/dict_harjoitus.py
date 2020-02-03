d = {"cat": "kissa"}
while True:
    word = input("Word to search?")
    if len(word) == 0:
        break
    if word in d:
        print(d[word])
    else:
        definition = input(word+" not found. Give definition for "+word+"?")
        if definition:
            d[word] = definition
