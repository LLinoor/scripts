## Language :
Python.

## Requiremnts : 
- FFMPEG (in PATH for Windows users.)
- `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

## How to use :
To retrieve and download the video from the iQiyi servers, you will need to fetch the DASH file of your video.

- Step 1 : Go to [iQiyi](https://iq.com)

- Step 2 : Go to the WebTools of your browser (F12 or Ctrl+Shift+I) and go to the Network tab.

![Step 2 in picture](https://github.com/LLinoor/scripts/blob/main/iqiyi-dl/resources/1.png?raw=true)

- Step 3 : Go to the episode you want to download (example: https://www.iq.com/play/11kx751cbrg)

- Step 4 : Search for "dash" in the Network tab you opened previously

- Step 5 : Right click on the result and Copy > Copy link address

![Step 5 in picture](https://github.com/LLinoor/scripts/blob/main/iqiyi-dl/resources/2.png?raw=true)

- Step 6 : Paste the link when the script asks you to.

## Warnings and explanations :

### Warning :

YT-DL is supposed to support iQiyi by default however YT-DL doesn't detect iQiyi links and therefore uses its basic scraper. You can look on your side if YT-DL works again, it will be much more convenient for you to use it instead of this script.

When YT-DL downloads the video, it will show you **a lot** of errors, despite that **the video downloads anyway**, so ignore these errors.

The script sends a .m3u8 file to decentralized servers allowing you to download the video with YT-DL.

### Explanations : 

The script makes a **.m3u8** file from the **DASH** file it uploads on [Siasky](https://siasky.net/), then it downloads the episode with **Youtube-DL (YT-DL)** in MPEG-TS format (lossless). Finally, the script downloads the English subtitles and uses **FFMPEG** to attach the subtitles to the video.
