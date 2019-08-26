from urllib.request import urlopen
url = "https://upload.wikimedia.org/wikipedia/commons/b/b9/CyprusShorthair.jpg"
url = "https://bit.ly/2T7BDAP"
with urlopen(url) as response:
    data = response.read()
    with open("cat.jpg", "wb") as f: # open write (binary) mode
        f.write(data)
    
