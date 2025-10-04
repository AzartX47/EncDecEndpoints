import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive"
}

API = "https://enc-dec.app/api"

'''
Server     Language     URL
-----------------------------------------------------------------------------------------------
Neon       Original     https://api.videasy.net/myflixerzupcloud/sources-with-title
Sage       Original     https://api.videasy.net/1movies/sources-with-title
Cypher     Original     https://api.videasy.net/moviebox/sources-with-title
Yoru       Original     https://api.videasy.net/cdn/sources-with-title  [MOVIE ONLY]
Reyna      Original     https://api2.videasy.net/primewire/sources-with-title
Omen       Original     https://api.videasy.net/onionplay/sources-with-title
Breach     Original     https://api.videasy.net/m4uhd/sources-with-title
Vyse       Original     https://api.videasy.net/hdmovie/sources-with-title
Killjoy    German       https://api.videasy.net/meine/sources-with-title?language=german
Harbor     Italian      https://api.videasy.net/meine/sources-with-title?language=italian
Chamber    French       https://api.videasy.net/meine/sources-with-title?language=french  [MOVIE ONLY]
Fade       Hindi        https://api.videasy.net/hdmovie/sources-with-title
Gekko      Latin        https://api2.videasy.net/cuevana-latino/sources-with-title
Kayo       Spanish      https://api2.videasy.net/cuevana-spanish/sources-with-title
Raze       Portugese    https://api.videasy.net/superflix/sources-with-title
Phoenix    Portugese    https://api2.videasy.net/overflix/sources-with-title
Astra      Portugese    https://api.videasy.net/visioncine/sources-with-title
'''

# Movie format: <https://api.videasy.net/{server}/sources-with-title?title={title}&mediaType=movie&year={year}&tmdbId={tmdb_id}&imdbId={imdb_id}>
# Tv format: <https://api.videasy.net/{server}/sources-with-title?title={title}&mediaType=tv&year={year}&tmdbId={tmdb_id}&imdbId={imdb_id}&episodeId={episode_number}&seasonId={season_number}>

# --- Cyberpunk Edgerunners ---
tmdb_id = "105248"
url = "https://api.videasy.net/myflixerzupcloud/sources-with-title?title=Cyberpunk%253A%2520Edgerunners&mediaType=tv&year=2022&tmdbId=105248&imdbId=tt12590266&episodeId=1&seasonId=1"

# Get encrypted text
enc_data = requests.get(url, headers=HEADERS).text
print(enc_data)
# Decrypt
decrypted = requests.post(f"{API}/dec-videasy", json={"text": enc_data, "id": tmdb_id}).json()['result']

print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(decrypted)
