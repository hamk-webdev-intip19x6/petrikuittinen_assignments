import json

d = {"name": "example ÄÖ", "number": 123, "list": [1, 2, 3]}
s = json.dumps(d) # s is string in JSON format containing data from d
print(s)

