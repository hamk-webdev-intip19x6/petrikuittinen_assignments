# World's Worst Web Browser

from functools import lru_cache
from urllib.request import urlopen, HTTPError
@lru_cache(maxsize=64)
def get_url(url):
    'Retrieve URL'
    try:
        with urlopen(url) as s:
            return s.read().decode("utf-8")
    except HTTPError:
        return 'Not Found'

    
while True:
    url = input("Give me URL?")
    if not url: break
    print(get_url(url)[:1000])

    
print(get_url.cache_info())


