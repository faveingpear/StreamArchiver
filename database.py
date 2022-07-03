import base64
from datetime import date
from encodings import utf_8
from this import s

class stream:

    filepath: str
    dateArchived: str
    link: str
    hash: str
    source: int

    def __init__(self, filepath, dateArchived, link, source, hash = None) -> None:
        self.filepath = filepath
        self.dateArchived = dateArchived
        self.link = link

        if hash == None:
            self.hash = self.genHash(link)
        else:
            self.hash = hash

        self.source = source

    def genHash(self, link):
        return base64.b64encode(bytes(link, "utf_8"))

class database(dict):

    dataBasePath: str

    def __init__(self, dataBasePath):
        super(database, self).__init__()
        self.__dict__ = self
        self.dataBasePath = dataBasePath

        try:
            self.loadDataBase(self.dataBasePath)
        except FileNotFoundError:
            print("Database not found, creating a new database")
            self.createNewDatabase(self.dataBasePath)

    def loadDataBase(self, path):
        file = open(path + "database.json", "r")
        data = file.read()
        file.close()

    def createNewDatabase(self, path):
        file = open(path + "database.json", "x")
        file.write("")
        file.close()

    def addEntry(self, streamObject):
        print("Added Entry " + str(streamObject.hash) )
        self.__dict__[streamObject.hash] = streamObject

if __name__ == "__main__":
    testStream = stream("~/Projects/video.mp4", "070222", "link", 1)
    print(testStream.hash)
    db = database("/home/mpearsonindyx/Projects/StreamArchiver/")
    db.addEntry(testStream)
    print(db)