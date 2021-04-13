from config import Config
from snake import Snake
from apple import Apple
import pygame,sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH,Config.WINDOW_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf',18)
        pygame.display.set_caption('Worm')
        self.apple = Apple()
        self.snake = Snake()

    def drawGrid(self):
        for x in range(0,Config.WINDOW_WIDTH,Config.CELLSIZE):
            #vertical lines
            pygame.draw.line(self.screen, Config.DARKGREY,
                (x,0),(x,Config.WINDOW_HEIGHT)
            )
        
        for y in range(0,Config.WINDOW_HEIGHT, Config.CELLSIZE):
            #horizontal lines
            pygame.draw.line(self.screen, Config.DARKGREY,
                (0,y),(Config.WINDOW_WIDTH,y)
            )


    def drawWorm(self):
        for coord in self.snake.wormCords:
            x = coord['x'] * Config.CELLSIZE
            y = coord['y'] * Config.CELLSIZE
            wormSegmentRect = pygame.Rect(
                x,y, Config.CELLSIZE, Config.CELLSIZE
            )
            pygame.draw.rect(self.screen, Config.DARKGREEN,wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(
                x+4,y+4,Config.CELLSIZE-8,Config.CELLSIZE-8
            )
            pygame.draw.rect(self.screen,Config.GREEN,wormInnerSegmentRect)

    def drawApple(self):
        x = self.apple.x *Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE
        appleRect = pygame.Rect(
            x,y, Config.CELLSIZE, Config.CELLSIZE
        )
        pygame.draw.rect(self.screen, Config.RED,appleRect)

    def drawScore(self,score):
        scoreSurf = self.BASICFONT.render('SCORE : %s' %(score),True,Config.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (Config.WINDOW_WIDTH -120,10)
        self.screen.blit(scoreSurf,scoreRect)

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.drawGrid()
        self.drawWorm()
        self.drawApple()
        self.drawScore(len(self.snake.wormCords)-3)
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def checkForKeyPress(self):
        if len(pygame.event.get(pygame.QUIT))>0:
            pygame.quit()
        keyUpEvents = pygame.event.get(pygame.KEYUP)
        if len(keyUpEvents) == 0:
            return None

        if keyUpEvents[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        
        return keyUpEvents[0].key

    def handelKeyEvents(self,event):

        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
            self.snake.direction = self.snake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
            self.snake.direction = self.snake.RIGHT

        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.UP
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
            self.snake.direction = self.snake.DOWN
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
    
    def resetGame(self):
        del self.apple
        del self.snake
        self.snake = Snake()
        self.apple = Apple()

        return True

    def drawPressKeyMsg(self):
        pressKeySurf = self.BASICFONT.render('Press a key to continue playing',True,Config.WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (Config.WINDOW_WIDTH -200,Config.WINDOW_HEIGHT-30)
        self.screen.blit(pressKeySurf,pressKeyRect)

    def isGameOver(self):
        if(self.snake.wormCords[self.snake.HEAD]['x']==-1 or
        self.snake.wormCords[self.snake.HEAD]['x']==Config.CELLWIDTH or
        self.snake.wormCords[self.snake.HEAD]['y']==-1 or
        self.snake.wormCords[self.snake.HEAD]['y']== Config.CELLHEIGHT):
            return self.resetGame()

        for wormBody in self.snake.wormCords[1:]:
            if wormBody['x'] == self.snake.wormCords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCords[self.snake.HEAD]['y']:
                return self.resetGame()

    def displayGameOver(self):
        gameoverFont = pygame.font.Font('freesansbold.ttf',150)
        gameSurf =gameoverFont.render('GAME', True,Config.WHITE)
        overSurf = gameoverFont.render('OVER',True,Config.WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (Config.WINDOW_WIDTH /2 ,10)
        overRect.midtop = (Config.WINDOW_WIDTH /2,gameRect.height +10+25)
        self.screen.blit(gameSurf,gameRect)
        self.screen.blit(overSurf,overRect)

        self.drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)
        self.checkForKeyPress()
        while True:
            if self.checkForKeyPress():
                pygame.event.get()
                return 

    def showStartScreen(self):
        titleFont = pygame.font.Font('freesansbold.ttf',100)
        titleSurf1 = titleFont.render('WORMYY!!',True,Config.WHITE,Config.DARKGREEN)
        titleSurf2 = titleFont.render('WORMYY!!',True,Config.GREEN)
        degrees1=0
        degrees2=0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
            self.screen.fill(Config.BG_COLOR)

            rotatedSurface1= pygame.transform.rotate(titleSurf1,degrees1)
            rotatedRect1 = rotatedSurface1.get_rect()
            rotatedRect1.center = (Config.WINDOW_WIDTH/2,Config.WINDOW_HEIGHT/2)
            self.screen.blit(rotatedSurface1,rotatedRect1)

            rotatedSurface2= pygame.transform.rotate(titleSurf2,degrees2)
            rotatedRect2 = rotatedSurface2.get_rect()
            rotatedRect2.center = (Config.WINDOW_WIDTH/2,Config.WINDOW_HEIGHT/2)
            self.screen.blit(rotatedSurface2,rotatedRect2)

            self.drawPressKeyMsg()

            pygame.display.update()
            self.clock.tick(Config.MENU_FPS)
            degrees1 +=1
            degrees2 +=2

    def run(self):
        self.showStartScreen()

        while True:
            self.gameloop()
            self.displayGameOver()

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    self.handelKeyEvents(event)
            
            self.snake.update(self.apple)
            self.draw()
            if self.isGameOver():
                break