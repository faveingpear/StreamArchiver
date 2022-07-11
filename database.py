from asyncio.log import logger
import base64
from datetime import date
from encodings import utf_8

from json import JSONEncoder
import json
from matplotlib.font_manager import json_dump

from numpy import source
from sympy import false, true

from logger import MyLogger

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.to_json()

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

        self.logger.info("[stream] created stream object " + self.hash)

    def genHash(self, link):
        return base64.b64encode(bytes(link, "utf_8"))

    def __iter__(self):
        yield from {
            "filepath": self.filepath,
            "dateArchived": self.dateArchived,
            "link": self.link,
            "source": self.source,
            "hash": self.hash
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        jsonData = {
            "filepath": self.filepath,
            "dateArchived": self.dateArchived,
            "link": self.link,
            "source": self.source,
            "hash": self.hash
        }
        return jsonData
class database():

    def __init__(self, logger, dataBasePath=None) -> None:
        self.logger = logger
        self.logger.info("[database] database is initialized")

        self.db = {}

        if dataBasePath == None:
            self.dataBasePath = "database.json"
        else:
            self.dataBasePath = dataBasePath

        self.db["dataBasePath"] = self.dataBasePath
        self.db["database"] = {}

        if self.loadDatabase() == True:
            pass
        else:
            self.logger.info("[database] No database file found, creating new database file at " + self.dataBasePath)
            self.createDataBaseFile()
        
    def addEntry(self, streamObject):
        self.logger.info("[database] Added Entry " + str(streamObject.hash))
        self.db["database"][streamObject.hash] = streamObject

    # def __iter__(self):
    #     yield from {
    #         "dataBasePath": self.dataBasePath,
    #         "database": self.db
    #     }.items()

    # def __str__(self):
    #     return json.dumps(dict(self), ensure_ascii=False)

    # def __repr__(self):
    #     return self.__str__()
    
    def to_json(self):

        streamDict = {}

        #print(self.db)

        for stream in self.db["database"]:
            streamDict[stream] = self.db["database"][stream].to_json()

        jsonData = {
            "dataBasePath": self.dataBasePath,
            "database": streamDict
        }
        return jsonData

    def createDataBaseFile(self):
        open(self.dataBasePath, "x")
    
    def saveDatabase(self):

        self.logger.info("[database] Saveing database")

        file = open(self.dataBasePath, "w")
        file.write(json.dumps(self, cls=MyEncoder))
        file.close()

        self.logger.info("[database] Database saved to " + self.dataBasePath)

    def loadDatabase(self) -> bool:

        self.logger.info("[database] loading database from " + self.dataBasePath)

        try:
            file = open(self.dataBasePath, "r")
        except Exception as e:
            self.logger.error("[database] Could not load database")
            self.logger.error(e)
            return false

        ## TODO
        ## Fix case where database file is present but no json data
        data = json.load(file)
        file.close()

        self.db["dataBasePath"] = data["dataBasePath"]
        self.db["database"] = {}

        for object in data["database"]:
            self.logger.info("[database] loading stream " + object)
            #print(type(data["database"][object]))
            self.db["database"][object] = stream(
                dateArchived=data["database"][object]["dateArchived"],
                link=data["database"][object]["link"],
                source=data["database"][object]["source"],
                filepath=data["database"][object]["filepath"],
                hash=data["database"][object]["hash"],
                logger=self.logger
            )
            self.logger.info("[database] Added stream " + data["database"][object]["hash"] + " to the database")

        return true

if __name__ == "__main__":
    databaseLogger = MyLogger(logFile="logging.log", name="database")
    db = database(dataBasePath="/home/faveing/Documents/gits/StreamArchiver/database.json",logger=databaseLogger)

    #testStream = stream(filepath="/test", dateArchived="06/10/2022", link="Https://blah", source=2, logger=logger)
    #testStream2 = stream(filepath="/test", dateArchived="06/10/2022", link="fdsaf://blah", source=2, logger=logger)
    #db.addEntry(testStream)
    #.addEntry(testStream2)
    print(db.to_json())
    db.saveDatabase()
    #db.loadDatabase()

    #print(json.dumps(db, cls=MyEncoder))