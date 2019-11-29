import time

class MyTime(object):

    def __init__(self):
        
        self.startTime = None
        self.elapsedTime = 0

    def start(self):
        self.startTime = time.time()*1000

    def stop(self):
        if self.startTime:
            stop = time.time()*1000
            self.elapsedTime += int(round(stop - self.startTime))
            self.startTime = None

    def timeElapsed(self):
        if (self.startTime):
            self.stop()
       
        return self.elapsedTime

    def reset(self):
        self.startTime = None
        self.elapsedTime = 0

