import requests
import re
from urllib.parse import urlparse

video_url = input("Insert Tiktok URL: ") 

api_url = "https://www.tikwm.com/api/"
params = {"url": video_url}

response = requests.get(api_url, params=params)
data = response.json()

if data.get("data"):
    download_url = data["data"]["play"]
    print("link video asli: ", download_url)
else:
    print("gagall", data)
