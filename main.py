import requests
import os
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("API_KEY")

query = "hot by young thug"

base_url = 'https://www.googleapis.com/youtube/v3/search'
params = {
    "part": "snippet",
    "q": query,
    "key": api_key
}

response = requests.get(base_url, params=params)
data = response.json()
youtube_video = []
for item in data['items']:
    video_title = item['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
    youtube_video.append(video_url)
    print(f'Title: {video_title}\nURL: {video_url}\n')

# print(youtube_video[0])
yt = YouTube(url=youtube_video[0])

# print(yt.title)
stream = yt.streams.filter(progressive=False)
# chosen_stream = stream.get_highest_resolution()
# chosen_stream.download()