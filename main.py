from pytube import YouTube
import os

def download(link, path):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        yt.download(path)
    except:
        print('An error has occurred.')
    print('Download is completed successfully.')

link = input('Enter the YouTube video URL: ')
path = input('Enter the path to store file: ')
download(link, path)