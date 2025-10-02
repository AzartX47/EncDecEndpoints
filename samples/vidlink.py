import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive",
    "Referer": "https://vidlink.pro/" # Set Referer to load streams
}

API = "https://enc-dec.app/api"

# Movie format: <https://vidlink.pro/api/b/movie/{encrypted_id}>
# Tv format: <https://vidlink.pro/api/b/tv/{encrypted_id}/{season_number}/{episode_number}>

# --- Cyberpunk Edgerunners ---
tmdb_id = "105248"

# Get encrypted tmdb id text
encrypted = requests.get(f"{API}/enc-vidlink?text={tmdb_id}").json()['result']

# Request vidlink url for S01E01
url = f"https://vidlink.pro/api/b/tv/{encrypted}/1/1"
data = requests.get(url, headers=HEADERS).json()

print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(data)