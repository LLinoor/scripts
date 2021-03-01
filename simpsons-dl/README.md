# simpsons-dl

**simpsons-dl** is a tool to download all episodes of The Simpsons (in **english** or **french**). The script will retrieve the episodes on the websites : simpson-en-streaming.com for French Version* and https://pixa-club.com/en/the-simpsons/ for English Version.

### Requirements:
- [Python 3.6 or higher](https://www.python.org/downloads/)
- `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

### How to use it:
- `main.py (-en/-fr) -e`
   - This argument allows you to download episode by episode. 
    
- `main.py (-en/-fr) -s`
   - This argument allows you to download season by season. 

#### Example : 
        python main.py -en -e
        Season ?
        24
        22 episodes found for this season
        Episode ?
        8
        ---------------------DOWNLOAD---------------------
        [generic] S24E08EN: Requesting header
        [generic] S24E08EN: Downloading webpage
        [generic] 8-epizod-8-to-cur-with-love-EN: Requesting header
        [download] Destination: The Simpson\The Simpson - S24E8.mp4
        [download] 0.3% of 72.63MiB at 509.15KiB/s ETA 02:25

### Bugs :

If you have problems, you can activate the verbose mode: `-v` (at the end of your command). 
However, this "verbose mode" will simply display youtube-dl errors and warnings. If you still can't identify your problem you can add the verbose mode of youtube-dl in the "ydl_opts".

Once you've identified the problem, you can report it on GitHub.

## Warning :
For security reasons, the links to download the French episodes are contained in a .json file and are not retrieved from simpson-en-streaming.com
