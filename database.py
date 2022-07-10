from asyncio.log import logger
import base64
from datetime import date
from encodings import utf_8

from json import JSONEncoder
import json

from logger import MyLogger

# class MyEncoder(JSONEncoder):
#     def default(self, obj):
#         return obj.__iter__  

class stream():

    def __init__(self, filepath, dateArchived, link, source, logger, hash = None) -> None:

        self.filepath = filepath
        self.dateArchived = dateArchived
        self.link = link
        self.source = source
        self.logger = logger

        if hash == None:
            self.hash = str(self.genHash(link))
        else:
            self.hash = hash

    def genHash(self, link):
        return base64.b64encode(bytes(link, "utf_8"))

    def __iter__(self):
        yield from {
            "fliepath": self.filepath,
            "dateArchived": self.dateArchived,
            "link": self.link,
            "source": self.source,
            "hash": self.hash
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class database():

    def __init__(self, dataBasePath, logger) -> None:
        self.logger = logger
        self.dataBasePath = dataBasePath

        self.logger.info("[database] database is being initialized")

        self.db = {}
        
    def addEntry(self, streamObject):
        self.logger.info("[database] Added Entry " + str(streamObject.hash))
        self.db[streamObject.hash] = streamObject

    def __iter__(self):
        yield from {
            "dataBasePath": self.dataBasePath,
            "database": self.db
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    #testStream = stream("~/Projects/video.mp4", "070222", "link", 1)

    databaseLogger = MyLogger(logFile="logging.log", name="database")

    db = database(dataBasePath="database.json",logger=databaseLogger)

    testStream = stream(filepath="~/test", dateArchived="06/10/2022", link="Https://blah", source=2, logger=logger)
    db.addEntry(testStream)
    #print(db)
    print(testStream)
    print(json.dumps(testStream, cls=MyEncoder))