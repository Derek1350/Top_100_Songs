import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import bs4
from bs4 import BeautifulSoup
CLIENT_ID = "c1d08315a1d6428ca10982e127609784"
CLIENT_SECRET = "a95d73741d93442cbab0cf8a6068e0ca"
REDIRECT_URI="https://example.com/"
USERNAME="2n3vohg923lg7ustb6fang577"
scope="playlist-modify-private"
access_token= "BQDhdYSeykQxmAFXBam1JgrE_LAAi9QttaNxZOCiWjRoYGBFDSkipp2qdfLuB8Mp4HeC41uhZLZMbC9U1k6jvdl89GvOJesqiQ6m5xG-l7LuiL2N5fz6dzs5r92Uf6bhQN8v419HU5bCTS80cYTAlOo-vxi1IhplBnLuZxoJgnx-Q6aN96rGFcCjNAZuQRJ-k8xZ4kZ9DtXs2FhbucZu6Bp5rrikFes_v6R9aA"
spotify=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=scope,redirect_uri=REDIRECT_URI,username=USERNAME))
USER_ID=spotify.current_user()["id"]
date=input("Enter the date or era You want to travel in format(yyyy-mm-dd)")
bs4_response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
page=bs4_response.text
soup=BeautifulSoup(page,"html.parser")
bs4_data=soup.select(selector=".o-chart-results-list__item>h3#title-of-a-story.c-title")
bs4_name=[' '.join(i.getText().split()) for i in bs4_data]
song_uri=[]
# to get uri 
for names in bs4_name:
    search_results = spotify.search(q=f"track:{names}") 
    try:
        uri = search_results["tracks"]["items"][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{names} doesn't exist in Spotify. Skipped.")

playlist=spotify.user_playlist_create(user=USERNAME,name=f"{date} TOP 100 SONGS",public=False)
id=playlist["id"]
with open("Song_name.txt","w") as file:
    for i in bs4_name:
        file.write(f"{i}\n")
spotify.playlist_add_items(playlist_id=id,items=song_uri)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # # Extract the URI of the first track in the search results
    # if names in search_results and 'items' in search_results['tracks']:
    #     first_track = search_results['tracks']['items'][0]
    #     track_uri = first_track['uri']
    #     print(f"URI of the song '{song_name}' by '{artist_name}': {track_uri}")
    # else:
    #     print(f"Song '{song_name}' by '{artist_name}' not found.")
# access_token="BQBotZhLUh4vRXck2zQ7gmEa3aaq2TH2I3bOXqsOwrAMgd8l1Bmlt3Xe55deGH_RGaX2EicS5py1_eS0ZGTGuV6eGPoA4BkpYOnC8b19_uQHW_bU66Cvr3aHoGFBGnu2PQvgMYhap8ggpQPACqwdjUdrj6Ssy-JrE2KFVexp3wNF82bejDRmZlRkMJP8LaMlLA3bK8mdZvpAK5ZJQ51QXb-IruYqE6iaWA"
# api_url="https://api.spotify.com/v1/users/2n3vohg923lg7ustb6fang577/playlists"
# api_params={
#     "name":"Top 100",
#     "public":False,
#     "description": "New playlist description"
# }

# response=requests.post(url=api_url,json=api_params,headers=api_headers)
# print(response.json())