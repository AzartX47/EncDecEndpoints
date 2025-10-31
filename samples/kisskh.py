import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "plain/text"
}

API = "https://enc-dec.app/api"

# --- KissKH ---

content_id = "192143"

# Get streams content
vid_key = requests.get(f"{API}/enc-kisskh?text={content_id}&type=vid").json()['result']
url = f"https://kisskh.do/api/DramaList/Episode/{content_id}.png?err=false&ts=&time=&kkey={vid_key}"
video_response = requests.get(url, headers=HEADERS).json()

# Get subtitles content
sub_key = requests.get(f"{API}/enc-kisskh?text={content_id}&type=sub").json()['result']
url = f"https://kisskh.do/api/Sub/{content_id}?kkey={sub_key}"
subtitle_response = requests.get(url, headers=HEADERS).json()

print(f"\n{'-'*25} Sample Response Data {'-'*25}\n")
print(video_response)
print(subtitle_response)