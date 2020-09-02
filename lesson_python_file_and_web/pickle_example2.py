import pickle
with open("mydata.pickle", "rb") as f:
    obj = pickle.load(f)
    print(obj)
    