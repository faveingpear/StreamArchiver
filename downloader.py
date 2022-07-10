from yt_dlp import YoutubeDL
from database import database
from database import stream

from logger import MyLogger

class Downloader():

    def __init__(self, logger) -> None:
        self.logger = logger

    def download(self, link):

        self.logger.info("[downloader] Downloading " + link)

        yt_opts = {
            'logger': self.logger
        }

        with YoutubeDL(yt_opts) as ydl:
            try:
                ydl.download(link)
            except Exception as e:
                self.logger.error("[downloader] ytdl error " + str(e))
                pass

            self.logger.info("[downloader] finished downloading " + link)

if __name__ == "__main__":
    print("Test")
    logger = MyLogger(logFile="logging.log", name="downloader")

    download = Downloader(logger=logger)
    download.download("https://www.youtube.com/watch?v=SLBfEwPHS6Y")
    


