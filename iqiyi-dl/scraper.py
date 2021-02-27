import re
import requests
import json
import youtube_dl
import os

manifest = input("DASH url ? \n")

response = requests.get(manifest)
embed = json.loads(response.text)
data = embed["data"]
program = data["program"]
video = program["video"]
for select in video:
    try:
        m3u8_test = select["m3u8"]
    except: 
        pass
    else:
        m3u8 = select["m3u8"]

result = m3u8.split("\\n")

with open("index.m3u8", "w") as file:
    for line in result :
        line = re.sub(r"\\/", "/", line)
        line = line + "\n"
        file.write(line)

stl = program["stl"]
for subtitles in stl:
    if (subtitles["_name"] == "English"):
        stllink = subtitles["srt"]
        stllink = re.sub(r"\\/", "/", stllink)
        stllink = "http://meta.video.iqiyi.com" + stllink
        response = requests.get(stllink)
        with open("subtitle.srt", "w", encoding="utf-8") as file : 
            file.write(response.text)

files = {
    'file': ('index.m3u8', open('index.m3u8', 'rb')),
}

response = requests.post('https://siasky.net/skynet/skyfile', files=files)
embed = json.loads(response.text)
downloadLink = "https://siasky.net/" + embed["skylink"]

ydl_opts = {
            'outtmpl': "episode.ts",
        }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([downloadLink])
    except:
        print("Unable to download the episode")
    else:
        os.system("ffmpeg -i .\episode.ts -i .\subtitle.srt -map 0:v -map 0:a -map 1:s -c:v copy -c:a copy -c:s copy output.mkv")
        os.system("rm episode.ts")
        
print("Finish.")