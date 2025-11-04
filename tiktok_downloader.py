import requests

video_url = input("Masukan url video: ")

api_url = "https://www.tikwm.com/api/"
params = {"url": video_url}

response = requests.get(api_url, params=params)
data = response.json()


if 'hdplay' in data['data'] and data['data']['hdplay']:
    download_url = data['data']['hdplay']
    print("Downloaing Video with HD Quality")
else:
    download_url = data['data']['play']
    print("Downloading with standart Quality")



video_response = requests.get(download_url, stream=True)

if video_response.status_code == 200:
    total_size = int(video_response.headers.get('Content-Length', 0))
    Downloaded = 0

    with open("video.mp4", "wb") as file:
        for chunk in video_response.iter_content(1024):
            if chunk:
                file.write(chunk)
                Downloaded += len(chunk)
                if total_size != 0:
                    percent = (Downloaded / total_size) * 100
                    print(f"\rDownloaded{Downloaded} bytes", end="")
    print("\nDownload selesai")
else:
    print("gagal download", video_response.status_code)






