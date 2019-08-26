import sys, json
def loadDictionary(filePath):
    """Load dictionary from JSON file. Return the contents or None if fails."""
    try:
        with open(filePath, "r") as f:
            return json.load(f)    
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return None

def saveDictionary(dictionary, filePath):
    """Save dictionary into JSON file. Return False if fails, otherwise True"""
    try:
        with open(filePath, "w") as f:
            json.dump(dictionary, f)
            return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False
        
DICTIONARY_FILE = "mydict.json"
d = loadDictionary(DICTIONARY_FILE)
if d:
    print("Dictionary loaded successful with", len(d), "words")
else:
    d = {"cat": "kissa"} # otherwise begin with this dictionary
while True:
    word = input("Give me a word?")
    if not word: break
    if word in d:
        print(word, "=", d[word])
    else:
        definition = input("Give definition for word %s?" % word)
        if definition:
            d[word] = definition

if saveDictionary(d, DICTIONARY_FILE):
    print("Dictionary saved successful with", len(d), "words")

