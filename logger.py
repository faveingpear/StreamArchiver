from cmath import log
import logging

class MyLogger:

    def __init__(self, logFile=None, name=None) -> None:

        if logFile == None:
            logging.basicConfig(filename="logging.log", filemode='x', encoding='utf-8', level=logging.INFO)
        else:
            logging.basicConfig(filename=logFile, filemode='w', encoding='utf-8', level=logging.INFO)

        if name == None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logging.getLogger(name)

    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        self.logger.error(msg)