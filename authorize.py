import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Secret ID"
REDIRECT_URI="https://example.com/"
USERNAME="2n3vohg923lg7ustb6fang577"
scope="playlist-modify-private"
spotify=spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=scope,redirect_uri=REDIRECT_URI,username=USERNAME)
spotify.get_access_token(as_dict=True)

#Zindagi ka pehla comment:::::YE CODE ACCESS TOKEN PRAPT KRNE KE LIYE JO KI 1HR MAI C**D JAEGA
