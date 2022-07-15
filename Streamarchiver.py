from database import database
from database import stream

from logger import MyLogger

from downloader import Downloader

import sys

DATABASEPATH = "/home/faveing/Documents/gits/StreamArchiver/database.json"

# yt_opts = {
    
# }

downloadLogger = MyLogger("logging.log", "downloader")
databaseLogger = MyLogger("logging.log", "database")
streamArchiverLogger= MyLogger("logging.log", "streamArchiver")

db = database(logger=databaseLogger, dataBasePath=DATABASEPATH)

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        
