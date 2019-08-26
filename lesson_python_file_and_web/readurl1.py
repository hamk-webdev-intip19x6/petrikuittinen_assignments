from urllib.request import urlopen
url = "https://yle.fi/uutiset"
with urlopen(url) as response:
    data = response.read().decode("utf-8")
    print(data[:1000]) # display only 1000 first characters
    
    
