import datetime
import json
import urllib.request

now = datetime.datetime.now()
today = "%d-%02d-%02d" % (now.year, now.month, now.day)
print(today)

url = "https://rata.digitraffic.fi/api/v1/trains/"+today
print(url)
with urllib.request.urlopen(url.strip()) as f:
    train_info = f.read().decode("utf-8")
    trains = json.loads(train_info, encoding="utf-8")
    print(trains)
    
    
