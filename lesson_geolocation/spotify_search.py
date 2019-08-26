import sys
# requires install of spotipy module, sudo pip install spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import json

search_str = raw_input("insert track to search?")

# Put your own client id and secret here, do NOT use these
client_id = "53e6b264343d4b8fb20413ac75eaf7ac"
client_secret = "a6b7a2afac2a45e798c0749541f9f2a1"

# get access token
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)
pprint.pprint(result)
