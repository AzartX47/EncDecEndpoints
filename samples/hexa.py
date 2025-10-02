import requests
from Crypto.Random import get_random_bytes

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "plain/text"
}

API = "https://enc-dec.app/api"

# Movie format: <https://themoviedb.hexa.watch/api/tmdb/movie/{tmdb_id}/images>
# Tv format: <https://themoviedb.hexa.watch/api/tmdb/tv/{tmdb_id}/season/{season_number}/episode/{episode_number}/images>

# --- Cyberpunk Edgerunners ---
url = "https://themoviedb.hexa.watch/api/tmdb/tv/105248/season/1/episode/1/images"

# Generate 32-byte hex key
key = get_random_bytes(32).hex()
HEADERS["X-Api-Key"] = key

# Get encrypted text
encrypted = requests.get(url, headers=HEADERS).text

# Decrypt
decrypted = requests.post(f"{API}/dec-hexa", json={"text": encrypted, "key": key}).json()['result']

print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(decrypted)