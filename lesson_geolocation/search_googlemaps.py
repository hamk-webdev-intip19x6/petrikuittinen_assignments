#!/usr/bin/python

import urllib, json
# do NOT use this one, use your own API key
api_key = "AIzaSyBv0pVN3QtrkcmqaN_5DJj4UUxbhTLnnBY"
latitude = 60.734051400000006
longitude = 24.798190899999998
radius = 5000 # meters
searchType = "restaurant" #// What to search for
address = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?\
location=%(latitude)f,%(longitude)f&radius=%(radius)d&type=%(searchType)s\
&key=%(api_key)s" % vars()
print(address)
f = urllib.urlopen(address)
data = f.read()
d = json.loads(data)
print(d)

