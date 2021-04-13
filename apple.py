import random
from config import Config

class Apple:
    def __init__(self): 
        self.setNewLocation()

    def setNewLocation(self):
        #random x and y coordinates
        self.x = random.randint(0,Config.CELLWIDTH -1)
        self.y = random.randint(0,Config.CELLHEIGHT-1)
