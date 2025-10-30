import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive"
}

API = "https://enc-dec.app/api"

# --- Cyberpunk Edgerunners ---
title = "Cyberpunk: Edgerunners"
type = "tv"
year = "2022"
imdb_id = "tt12590266"
tmdb_id = "105248"
season = "1"
episode = "1"

# Get token data to load player
token_data = requests.get(f"{API}/enc-vidstack").json()['result']

# Get player parts
player_url = f"https://api.smashystream.top/api/v1/videosmashyi/{imdb_id}/{tmdb_id}/{season}/{episode}?token={token_data['token']}&user_id={token_data['user_id']}"
response = requests.get(player_url, headers=HEADERS).json()
host, id = response['data'].split("/#")

# Get encrypted stream data
stream_url = f"{host}/api/v1/video?id={id}"
encrypted = requests.get(stream_url, headers=HEADERS).text

# Decrypt
decrypted = requests.post(f"{API}/dec-vidstack", json={"text": encrypted}).json()["result"]
print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(decrypted)
