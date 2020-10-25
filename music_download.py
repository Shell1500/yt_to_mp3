from __future__ import unicode_literals
# from multiprocessing import Queue
from bs4 import BeautifulSoup
from ask_directory import ask_directory
import requests
import youtube_dl



print('Made By Shell1500\n')

print('Credits to dstftw\n')


while True:

    final_link = []
    
    print('\nEnter The Song You want to Download Or Enter YouTube Playlist Link')
    user_input = input('> ')
    user_inputs = user_input.split(',')
    
    # checks if input is a playlist
    
    for user_input in user_inputs:
        if '?list=' in user_input or 'watch?v' in user_input:
            final_link.append(user_input)

    else:
        
        # get html from yt link
        search_links =[requests.get('https://www.youtube.com/results?search_query={}'.format(i)).text for i in user_inputs]

        for search_link in search_links:
            strt = search_link.find('watch?v=')
            end = strt+19
            final_link.append('https://www.youtube.com/' + search_link[strt:end])
        

    # create prompt to select download location
    save_location = ask_directory()

    print(final_link)

    print('Saving to {}\n'.format(save_location))

    # setting properties for yt-dl module
    # ydl_opts = {
    #     'format': 'bestaudio[ext=flv]',
    #     # output location
    #     'outtmpl': save_location + '/%(title)s.%(ext)s'
    # }


    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

    'outtmpl': save_location + '/%(title)s.%(ext)s'
}


    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(final_link)

    print('\nPress E to Exit Or Press Enter To Download another song Or Playlist')
    enter = input('> ')
    if enter == 'E' or enter == 'e':
        break
    
    
