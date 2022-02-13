import pygame
from Player import Player

class Enemy:

    health = 5
    width = 100
    height = 100 
    speed = 10
    isDead = False
    easing = .05


# health, width, height, speed, x, y, isDead
    def __init__(self, tempX, tempY):
        self.x = tempX
        self.y = tempY

    def render(self, aSurface):
        enemyRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(aSurface, (0, 0, 255), enemyRect)


        ## add easing function 
        ## enemies will ease towards the heroes(players)
    def ease(self, aPlayerX, aPlayerY):
        dx = aPlayerX - self.x
        self.x += dx * self.easing

        dy = aPlayerY - self.y
        self.y += dy * self.easing