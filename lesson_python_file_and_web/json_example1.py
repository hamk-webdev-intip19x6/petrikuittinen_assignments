import json

d = {"name": "example", "number": 123, "list": [1, 2, 3]}
with open("mydata.json", "w") as f:
    json.dump(d, f)
