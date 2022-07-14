from database import database
from database import stream

from logger import MyLogger

from downloader import Downloader

DATABASEPATH = "/home/faveing/Documents/gits/StreamArchiver/database.json"

yt_opts = {
    
}

downloadLogger = MyLogger("logging.log", "downloader")
databaseLogger = MyLogger("logging.log", "database")

db = database(logger=databaseLogger, dataBasePath=DATABASEPATH)
downloader = Downloader(logger=downloadLogger)

downloader.download(link="https://www.youtube.com/watch?v=IpzafkH7LEc")