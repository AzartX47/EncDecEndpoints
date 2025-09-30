import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Connection": "keep-alive"
}

API = "https://enc-dec.app/api"

# --- Cyberpunk Edgerunners ---
# Note that there are different servers, find them here: https://backend.xprime.tv/servers
backend = "https://backend.xprime.tv/primebox?name=Cyberpunk%3A+Edgerunners&year=2022&imdb=tt12590266&season=1&episode=1"

# Get encrypted text
encrypted = requests.get(backend, headers=HEADERS).text

# Decrypt
decrypted = requests.post(f"{API}/dec-xprime", json={"text": encrypted}).json()

print(f"\n{'-'*25} Decrypted Data {'-'*25}\n")
print(decrypted)