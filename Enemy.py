import pygame
from Player import Player
import random

class Enemy:

    health = 5
    width = 20
    height = 20 
    speed = random.randint(2,10)
    isDead = False
    easing = random.uniform(0.01, 0.06)
    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0



# health, width, height, speed, x, y, isDead
    def __init__(self, tempX, tempY):
        self.x = tempX
        self.y = tempY
        self.easing = random.uniform(0.01, 0.06)


    def render(self, aSurface):
        enemyRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(aSurface, (0, 0, 255), enemyRect)


        ## add easing function 
        ## enemies will ease towards the heroes(players)
    def ease(self, aPlayerX, aPlayerY):
        self.dx = aPlayerX - self.x
        self.x += self.dx * self.easing

        dy = aPlayerY - self.y
        self.y += dy * self.easing

    def resetEnemyBoundaries(self):
        self.topBound = self.y
        self.bottomBound = self.y + self.height
        self.leftBound = self.x
        self.rightBound = self.x + self.width

    def enemyHit(self, aPlayer):
        if(self.topBound < aPlayer.bottomBound):
            if(self.bottomBound > aPlayer.topBound):
                if(self.rightBound > aPlayer.leftBound):
                    if(self.leftBound < aPlayer.rightBound):
                        print("enemy is hit")

        # else: print ("not hit")

        

