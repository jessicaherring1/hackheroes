import pygame

class Player:

    health = 5
    width = 100
    height = 100
    speed = 10
    isDead = False

#health, width, height, speed, x, y, isDead
    def __init__(self, tempx, tempy):
        self.x = tempx
        self.y = tempy

    def render(self, aSurface):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(aSurface, (255,0,255), playerRect)

    