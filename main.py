import requests
import os
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("API_KEY")

query = input("What are you looking for? ")

def get_url(query, api_key):
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        "part": "snippet",
        "q": query,
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    snippet = data['items'][0]
    video_url = f'https://www.youtube.com/watch?v={snippet['id']['videoId']}'
    return video_url

video_url = get_url(query=query, api_key=api_key)
# for item in data['items']:
#     video_title = item['snippet']['title']
#     video_url = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
#     youtube_video.append(video_url)
#     print(f'Title: {video_title}\nURL: {video_url}\n')

def download_video(video):
    yt = YouTube(url=video)
    stream = yt.streams.filter(progressive=True)
    chosen_stream = stream.get_highest_resolution()
    chosen_stream.download(output_path="./videos")


def download_audio(audio):
    yt = YouTube(url=audio)
    audio_stream = yt.streams.filter(only_audio=True)
    audio = audio_stream.get_audio_only()
    audio.download(output_path="./songs")

try:
    download_video(video=video_url)
    download_audio(audio=video_url)
except:
    print("No such files!!")