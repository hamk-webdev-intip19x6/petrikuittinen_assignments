import pickle

d = {"name": "example", "number": 123, "list": [1, 2, 3]}
with open("mydata.db", "wb") as f:
    pickle.dump(d, f)
