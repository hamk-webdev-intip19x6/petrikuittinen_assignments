import json
with open("mydata.json", "r") as f:
    obj = json.load(f)
    print(obj)
    