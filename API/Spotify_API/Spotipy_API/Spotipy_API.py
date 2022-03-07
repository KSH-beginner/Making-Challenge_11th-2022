import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
 
cid = 'd46569c22e364e279530ee57b31a885e'
secret = '25e5d9c728704465ae97adca23062ebb'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search 기능
result = sp.search("iu", limit=2, type="artist,track")
items = result
pprint.pprint(items)


# # artist_albums 기능
# search_result = sp.search("iu", limit=1, type="artist")
# iu_ID = search_result["artists"]["items"][0]["id"]
# album_result = sp.artist_albums(iu_ID, limit=5)
# items = album_result["items"]
# pprint.pprint(items)

# # 앨범 id 추출
# album_IDs = []
# for item in items:
#     album_IDs.append(item["id"])
# print(album_IDs)

# for album_ID in album_IDs:
#     pprint.pprint()

# result = sp.album_tracks('01dPJcwyht77brL4JQiR8R', limit = 3)
# pprint.pprint(result)