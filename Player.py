from ctypes import sizeof
from re import X
from turtle import width
import pygame

class Player:

    health = 5
    width = 20
    height = 20
    isDead = False
    runSpeed = 5
    
    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0

    movingLeft = False
    movingRight = False
    movingUp = False
    movingDown = False


#health, width, height, speed, x, y, isDead
    def __init__(self, tempx, tempy):
        self.x = tempx
        self.y = tempy

    def render(self, aSurface): #CHANGE
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(aSurface, (255,0,255), playerRect)

    def renderWoman(self, aSurface): #CHANGE
        #womanAnimation.display(self.x, self.y)
        pass

    def renderMan(self, aSurface): #CHANGE
        #manAnimation.display(self.x, self.y)
        pass

    def move(self):
        if self.movingRight == True:
            self.x+= self.runSpeed
        if self.movingLeft == True:
            self.x-= self.runSpeed
        if self.movingUp:
            self.y-= self.runSpeed
        if self.movingDown:
            self.y+= self.runSpeed
        if self.x <= 0:
            self.x = 0
        # if self.x >= 800: #width of window
        #     self.x = 800 - self.width - 1
        if self.y < 0:
            self.y = 0
        if self.y >= 600: #height of window
            self.y = 600 - self.height

    
    def resetBoundaries(self):
        self.topBound = self.y
        self.bottomBound = self.y + self.height
        self.leftBound = self.x
        self.rightBound = self.x + self.width