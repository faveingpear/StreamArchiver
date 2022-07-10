from yt_dlp import YoutubeDL
from database import database
from database import stream

class Dowloader():

    def __init__(self) -> None:
        pass

    def download(self, yt_opts, link):
        with YoutubeDL(yt_opts) as ydl:
            ydl.download(link)

