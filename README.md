# yt_to_mp3
A simple app to download songs to your computer by entering the song name.

It uses `requests` and `bs4` to get the first result from youtube search and then uses `youtube-dl` to download the first song.

## Installation
Download the files
Then run `pip install -r requirements.txt`
Then run either `music_download_no_ffmpeg.py`(doesn't require ffmpeg, saves as webm) or  `music_download.py`(requires ffmpeg, saves as mp3)

To download multiple songs at once, seperate keywords with `,`
Example:
`song1, song2, song3`
