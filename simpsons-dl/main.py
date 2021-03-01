import youtube_dl
from requests_html import HTMLSession
import re
import sys
import json

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

try:
    language = sys.argv[1]
    arg = sys.argv[2]
except:
        print("""Arguments available:
        Language : 
            -en : English
            -fr : French

        Arguments : 
            -e = Download episode per episode
            -s = Download season per season
        """)
else:
    saison = "0"
    episode = "0"
    try: 
        verbose = sys.argv[3]
        if(verbose == '-v'):
            class MyLogger(object):
                def debug(self, msg):
                    print(msg)

                def warning(self, msg):
                    print(msg)

                def error(self, msg):
                    print(msg)

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'The Simpson/The Simpson - S{saison}E{episode}.mp4',
                'no_warnings' : True,
                'logger': MyLogger(),
                'verbose': True
            }
            
        print("Verbose mode enabled.")
    except:
        class MyLogger(object):
            def debug(self, msg):
                print(msg)

            def warning(self, msg):
                pass

            def error(self, msg):
                pass

        ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'The Simpson/The Simpson - S{saison}E{episode}.mp4',
                'no_warnings' : True,
                'logger': MyLogger()
            }

    def bypassLogin(saison, episode, link):
        if(int(saison) < 10):
            tmp = str(saison)
            if(tmp[0] == "0"):
                saison = saison[1:]
            seasonZero = "0" + str(saison)
        else: 
            seasonZero = str(saison)

        if(int(episode) < 10):
            tmp = str(episode)
            if(tmp[0] == "0"):
                episode = episode[1:]
            episodeZero = "0" + str(episode)
        else: 
            episodeZero = str(episode)

        ver1 = "https://pixavideo.club/video/simpsons/" + f"{saison}/S{seasonZero}E{episodeZero}EN.mp4"  

        link = link.split("/the-simpsons/")[1]
        linkSplited = link.split("/")
        linkSplited[1] = f"{episode}-" + linkSplited[1] + "-EN.mp4"
        ver2 = "https://pixavideo.club/video/the-simpsons/" + linkSplited[0] + "/" + linkSplited[1]

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([ver1])
        except:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([ver2])

    def englishEpisode():
        saison = input("Season ? \n")

        if(str(saison[0]) == "0"):
                saison = saison[1:]

        session = HTMLSession()
        url = f'http://pixa-club.com/en/the-simpsons/season-{saison}/'
        API = session.get(url)
        episodeURL = API.html.find("div.col-md-8 > div.row")
        links = episodeURL[0].absolute_links
        episodeLink = []

        for link in links:
            episodeLink.append(link)

        print(f"{len(episodeLink)} episodes found for this season")
        episodeLink.append("http://pixa-club.com/en/")
        episodeLink.sort(key=natural_keys)
        episode = input("Episode ? \n")

        if(str(episode[0]) == "0"):
                episode = episode[1:]

        print("---------------------DOWNLOAD---------------------")
        bypassLogin(saison, episode, episodeLink[int(episode)])

    def englishSeason():
        saison = input("Season ? \n")
        if(str(saison[0]) == "0"):
                    saison = saison[1:]

        session = HTMLSession()
        url = f'http://pixa-club.com/en/the-simpsons/season-{saison}/'
        API = session.get(url)
        episodeURL = API.html.find("div.col-md-8 > div.row")
        links = episodeURL[0].absolute_links
        episodeLink = []
        for link in links:
            episodeLink.append(link)
        print(f"{len(episodeLink)} episodes found for this season")
        episodeLink.append("http://pixa-club.com/en/")
        episodeLink.sort(key=natural_keys)
        episodes = len(episodeLink)

        print("---------------------DOWNLOAD---------------------")

        for episode in range(len(episodeLink)):
            episode = episode + 1
            print(f'{episode}/{episodes}')
            url = episodeLink[int(episode)]
            bypassLogin(saison, episode, url)

    def frenchEpisode():
        with open("links.json", "r") as json_file :
            library = json.load(json_file)
            print("Répertoire chargé.")

        saison = input("Saison ? \n")

        if(str(saison[0]) == "0"):
                saison = saison[1:]

        print(f"{len(library[f'S{saison}'])} épisodes trouvés pour cette saison.")
        episode = input("Épisode ? \n") 

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'The Simpson/The Simpson - S{saison}E{episode}.mp4',
            'no_warnings' : True,
            'logger': MyLogger()
        }

        print("---------------------TÉLÉCHARGEMENT---------------------")

        session = HTMLSession()
        url = library[f'S{saison}'][f'E{episode}']
        API = session.get(url)
        API.html.render()

        downloadable = API.html.find('video#videoPlayer_html5_api > source')[0].attrs['src']

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([downloadable])
        except:
            print("Téléchargement échoué")
            print("Vous pouvez créer une issue sur Github : https://github.com/LLinoor/Simpson-Downloader")

    def frenchSeason():
        with open("links.json", "r") as json_file :
            library = json.load(json_file)
            print("Répertoire chargé.")

        saison = input("Saison ? \n")
        if(str(saison[0]) == "0"):
                saison = saison[1:]
        print(f"{len(library[f'S{saison}'])} épisodes trouvés pour cette saison.")

        print("---------------------TÉLÉCHARGEMENT---------------------")

        for episode in range(len(library[f'S{saison}'])):

            episode = episode + 1
            episode = str(episode)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'The Simpson/The Simpson - S{saison}E{episode}.mp4',
                'no_warnings' : True,
                'logger': MyLogger()
            }

            session = HTMLSession()
            url = library[f'S{saison}'][f'E{episode}']
            API = session.get(url)
            API.html.render()

            downloadable = API.html.find('video#videoPlayer_html5_api > source')[0].attrs['src']

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([downloadable])
            except:
                print("Téléchargement échoué")
                print("Vous pouvez créer une issue sur Github : https://github.com/LLinoor/Simpson-Downloader")

    if(language == '-en' and arg == '-e'):
        englishEpisode()

    elif(language == "-en" and arg == "-s"):
        englishSeason()

    elif(language == "-fr" and arg == "-e"):
        frenchEpisode()

    elif(language == "-fr" and arg == "-s"):
        frenchSeason()

    elif(language != '-en' or language !='-fr' or arg != '-e' or arg != '-s' or arg != '-u'):
        print("""Arguments available:
        Language : 
            -en : English
            -fr : French

        Arguments : 
            -e = Download episode per episode
            -s = Download season per season
        """)