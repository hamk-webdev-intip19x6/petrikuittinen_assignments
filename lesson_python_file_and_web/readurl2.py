from urllib.request import urlopen
url = "https://bit.ly/2T7BDAP"
with urlopen(url) as response:
    data = response.read()
    with open("cat.jpg", "wb") as f:
        f.write(data) 
