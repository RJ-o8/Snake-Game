from config import Config
import random

class Snake:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD =0

    def __init__(self):
        self.x = random.randint(5,Config.CELLWIDTH-6)
        self.y = random.randint(5,Config.CELLHEIGHT -6)
        self.direction = self.RIGHT
        self.wormCords = [
            {'x':self.x, 'y':self.y},
            {'x':self.x-1, 'y':self.y},
            {'x':self.x-2, 'y':self.y}
        ]

    def update(self,apple):
        #check if the snake has eaten a apple
        if self.wormCords[self.HEAD]['x'] == apple.x and self.wormCords[self.HEAD]['y'] == apple.y:
            apple.setNewLocation()
        else:
            del self.wormCords[-1]

        #move the worm by adding a block in the moving direction\
        if self.direction == self.UP:
            newHead = {
                'x':self.wormCords[self.HEAD]['x'],
                'y':self.wormCords[self.HEAD]['y'] -1
            }
        elif self.direction == self.DOWN:
            newHead = {
                'x':self.wormCords[self.HEAD]['x'],
                'y':self.wormCords[self.HEAD]['y'] + 1
            }

        elif self.direction == self.LEFT:
            newHead = {
                'x':self.wormCords[self.HEAD]['x'] -1,
                'y':self.wormCords[self.HEAD]['y']
            }
        elif self.direction == self.RIGHT:
            newHead = {
                'x':self.wormCords[self.HEAD]['x'] + 1,
                'y':self.wormCords[self.HEAD]['y']
            }

        self.wormCords.insert(0,newHead)