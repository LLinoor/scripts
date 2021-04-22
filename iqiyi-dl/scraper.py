import re
import requests
import json
import youtube_dl
import os
import platform
import random
import string
import datetime
import sys

def random_string():
    return ("".join(random.choice(string.ascii_letters) for i in range(10)))

def datetime_name():
    return "iqiyi_dl " + str(datetime.datetime.now().strftime("%Y-%M-%d %H:%M"))

try:
    arg = sys.argv[1]
except:
    skipFFMPEG = False
else: 
    if(arg == "-s"):
        skipFFMPEG = True
    else :
        skipFFMPEG = False

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

filename_index = random_string() + ".m3u8"
with open(filename_index, "w") as file:
    for line in result :
        line = re.sub(r"\\/", "/", line)
        line = line + "\n"
        file.write(line)

try:
    stl = program["stl"]
    for subtitles in stl:
        if (subtitles["_name"] == "English"):
            stllink = subtitles["srt"]
            stllink = re.sub(r"\\/", "/", stllink)
            stllink = "http://meta.video.iqiyi.com" + stllink
            response = requests.get(stllink)
            filename_subtitles = random_string() + ".srt"
            with open(filename_subtitles, "w", encoding="utf-8") as file : 
                file.write(response.text)
except:
    noSub = True
    print("No subtitles detected.")
else:
    noSub = False

files = {
    'file': ('index.m3u8', open(filename_index, 'rb')),
}

response = requests.post('https://siasky.net/skynet/skyfile', files=files)
embed = json.loads(response.text)
downloadLink = "https://siasky.net/" + embed["skylink"]

filename_stream = random_string() + ".ts"
ydl_opts = {
            'outtmpl': filename_stream,
        }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([downloadLink])
    except:
        print("Unable to download the episode, be sure that FFMPEG and all dependencies is installed")
    else:
        if(noSub == False):
            if(skipFFMPEG == False):
                os.system(f"ffmpeg -i {filename_stream} -i {filename_subtitles} -map 0:v -map 0:a -map 1:s -c:v copy -c:a copy -c:s copy '{datetime_name()}.mkv'")
                if(platform.system() == "Windows"):
                    os.system(f"del {filename_stream} && del {filename_subtitles} && del {filename_index}")
                elif(platform.system() == "Linux" or platform.system() == "Darwin"):
                    os.system(f"rm {filename_stream} && rm {filename_subtitles} && rm {filename_index}")
                else:
                    print(f"Unknown OS, {filename_stream}, {filename_subtitles} and {filename_index} has not been deleted.")
            else:
                print(f"Skip FFMPEG enabled, the video is in the {filename_stream} file and the subtitles in {filename_subtitles}.")
        else:
            print(f"No sub detected, the video is in the {filename_stream} file")

print("Finish.")