import pickle
with open("mydata.db", "rb") as f:
    obj = pickle.load(f)
    print(obj)
    