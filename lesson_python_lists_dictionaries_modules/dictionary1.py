# dictionary is basically a hash table, of the following syntax
# {key: value, key2: value2}
# where key can be any immutable data type e.g. string, number, tuple
# and value can be any type, including mutable types, such as lists or dictionaries
d  = {} # empty dictionary
d = {"cat": "kissa", "dog": "koira"} # define a dictionary with 2 key value pairs
print(d)
d["ape"] = "apina" # add a new key value pair
print(d["cat"])
d["cat"] = "mirri" # update existing key value pair
print(d["cat"])
if "cat" in d: # checking if something exists in a dictionary
    print("cat found")
print(d.values())
print(d.keys())
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for word, definition in d.items():
    print(word, "=", definition)
for word in sorted(d):
    print(word)
del d["dog"] # remove
