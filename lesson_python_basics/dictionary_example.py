d = {"cat": "kissa", "dog": "koira"}
d["mouse"] = "hiiri" # add more
if "whale" not in d:
    d["whale"] = "valas"
if "cat" in d:
    print(d["cat"])
del d["whale"]
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value, sep=" = ")

