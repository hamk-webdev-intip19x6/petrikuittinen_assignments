import json
s = '{"list": [1, 2, 3], "number": 123, "name": "example \u00c4\u00d6"}' # input string in JSON
obj = json.loads(s)
print(obj)

    