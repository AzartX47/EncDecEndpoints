import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive",
    "Referer": "https://mapple.uk/",
    "Next-Action": "4067783bff09863112a9a148953f77cd8fa3d8d72a" # Necessary header
}

API = "https://enc-dec.app/api"

# --- Arcane ---
title = "Arcane"
type = "tv"
year = "2021"
imdb_id = "tt11126994"
tmdb_id = "94605"
season = "1"
episode = "1"

'''
Sample API calls:
https://mapple.uk/watch/movie/181812 - Movie
https://mapple.uk/watch/tv/105248/1-1 - TV Show Season-Episode

Sources:

Mapple 4K - mapple
Sakura - sakura
Pinecone - alfa
Oak - oak
Willow - wiggles

Sample payload formats:
[{"mediaId": "181812", "mediaType": "movie", "tv_slug": "", "source": "_SOURCE_CODE_", "sessionId": "_SESSION_ID_"}] - Movie
[{"mediaId": "105248", "mediaType": "tv", "tv_slug": "1-1", "source": "_SOURCE_CODE_", "sessionId": "_SESSION_ID_"}] - TV Show
'''

# Get session ID
session_res = requests.get(f"{API}/enc-mapple", headers=HEADERS).json()
session_id = session_res['result']['sessionId']

# Build sample payload for tv series
payload = [{
    "mediaId": tmdb_id,
    "mediaType": "tv",
    "tv_slug": f"{season}-{episode}",
    "source": "mapple",
    "sessionId": session_id
}]

# Get data and parse streams
response = requests.post(f"https://mapple.uk/watch/tv/{tmdb_id}/{season}-{episode}", json=payload, headers=HEADERS).text
strams_data = response.split("\n")[1].replace("1:", "")
print(f"\n{'-'*25} Streams Data {'-'*25}\n")
print(strams_data)
