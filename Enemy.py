import pygame

class Enemy:

    health = 5
    width = 20
    height = 20 
    speed = 10
    isDead = False


# health, width, height, speed, x, y, isDead
    def __init__(self, tempX, tempY):
        self.x = tempX
        self.y = tempY

    def render(self, aSurface):
        enemyRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(aSurface, (0, 0, 255), enemyRect)


        ## add easing function 
        ## enemies will ease towards the heroes(players)