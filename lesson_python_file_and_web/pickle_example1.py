import pickle

d = {"name": "example ÄÖ", "number": 123, "list": [1, 2, 3]}
with open("mydata.pickle", "wb") as f:
    pickle.dump(d, f)
