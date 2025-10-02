import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive",
    "Origin": "https://xprime.tv" # Set Origin to load streams
}

API = "https://enc-dec.app/api"

# Note that there are different servers, find them here: https://backend.xprime.tv/servers
# Movie format: <https://backend.xprime.tv/{server}?name={title}&year={year}&id={tmdb_id}&imdb={imdb_id}>
# Tv format: <https://backend.xprime.tv/{server}?name={title}&year={year}&id={tmdb_id}&imdb={imdb_id}&season={season_number}&episode={episode_number}>

# --- Cyberpunk Edgerunners ---
url = "https://backend.xprime.tv/primebox?name=Cyberpunk%3A+Edgerunners&year=2022&id=105248&imdb=tt12590266&season=1&episode=1"

# Get encrypted text
encrypted = requests.get(url, headers=HEADERS).text

# Decrypt
decrypted = requests.post(f"{API}/dec-xprime", json={"text": encrypted}).json()['result']

print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(decrypted)