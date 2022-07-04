import base64
from datetime import date
from encodings import utf_8
from this import s

from sympy import false, true

import json

class stream(dict):

    def __init__(self, filepath, dateArchived, link, source, hash = None) -> None:
        super(stream, self).__init__()
        self.__dict__ = self
        
        self.__dict__["filepath"] = filepath
        self.__dict__["dateArchived"] = dateArchived
        self.__dict__["link"] = link
        self.__dict__["source"] = source

        if hash == None:
            self.__dict__["hash"] = str(self.genHash(link))
        else:
            self.__dict__["hash"] = hash

    def genHash(self, link):
        return base64.b64encode(bytes(link, "utf_8"))

class database(dict):

    dataBasePath: str

    def __init__(self, dataBasePath):
        super(database, self).__init__()
        self.__dict__ = self
        self.dataBasePath = dataBasePath

        self.loadDataBase(self.dataBasePath)


    def loadDataBase(self, path):
        try:
            file = open(path + "database.json", "r")
        except FileNotFoundError:
            print("FILE NOT FOUND ERROR")
            self.createNewDatabase(self.dataBasePath)
            pass
        data = json.load(file)
        file.close()

        for object in data:
            try:
                self.__dict__[data[object]["hash"]] = stream(
                    data[object]["filepath"],
                    data[object]["dateArchived"],
                    data[object]["link"],
                    data[object]["source"],
                    data[object]["hash"]
                )
            except Exception as e:
                print(e)

    def createNewDatabase(self, path):
        file = open(path + "database.json", "x")
        file.write("")
        file.close()

    def addEntry(self, streamObject):
        print("Added Entry " + str(streamObject.hash) )
        self.__dict__[streamObject.hash] = streamObject

    def saveEntry(self, path=None):

        if path == None:
            with open(self.dataBasePath + "database.json", "w") as outfile:
                json.dump(self.__dict__, outfile)
        else:
            pass

if __name__ == "__main__":
    testStream = stream("~/Projects/video.mp4", "070222", "link", 1)
    print(testStream.hash)
    db = database("/home/faveing/Documents/gits/StreamArchiver/")
    #db.addEntry(testStream)
    print(db)
    db.saveEntry()