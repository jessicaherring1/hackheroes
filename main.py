import pygame
from Player import Player

# Define the size of the game window
WIDTH = 1200
HEIGHT = 800
# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Best game")

FPS=60

player1= Player(200, 100)

# yellowShipImg = pygame.image.load("Assets/spaceship_yellow.png")
# redShipImg = pygame.image.load("Assets/spaceship_red.png")

def main():
    clock = pygame.time.Clock()

# make a boolean that represents whether the game should continue to run or not
    running = True


    # while the game is running
    while running:
        # this makes it so this function can run at most FPS times/sec
        clock.tick(FPS)

        # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
               pass

        player1.render(WINDOW)

        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

        if keysPressed[pygame.K_w]== True:
            player1.y-=player1.speed

        elif keysPressed[pygame.K_s]== True:
            player1.y+= player1.speed

        WINDOW.fill((0,0,0))
        # put code here that should be run every frame
         # of your game             
        pygame.display.update()
main()
