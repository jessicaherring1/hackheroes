import pygame
from Player import Player
from Enemy import Enemy 
from Button import Button


# Define the size of the game window
WIDTH = 800
HEIGHT = 530

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# clock = pygame.time.Clock

# dt = clock.tick()
# timeSinceLastEnemySpawn += dt
# if timeSinceLastEnemySpawn > 5000:
#     # spawn enemy
#     timeSinceLastEnemySpawn = 0

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # make the game window object

bg = pygame.image.load("background.jpg").convert()



pygame.display.set_caption("Hackheroes") # name the game window

FPS=60 # frames per second

player1= Player(200, 100)
enemy1 = Enemy(500, 500)
button1 = Button( 50, 50, 50, 50, (255, 0, 0), "hello")



state = 1

# yellowShipImg = pygame.image.load("Assets/spaceship_yellow.png")
# redShipImg = pygame.image.load("Assets/spaceship_red.png")

def main():
    clock = pygame.time.Clock()

    running = True #boolean that represents whether the game should continue to run or not

    # while the game is running
    while running:
        #WINDOW.fill((0,0,0))
        screen.blit(bg, [0, 0])
        
        clock.tick(FPS) # this makes it so this function can run at most FPS times/sec

        # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
               pass
        
        if state == 0: # home screen
            pass

        if state == 1: #game state (level 1)

            player1.render(WINDOW)
            player1.move()
            player1.resetBoundaries()
            enemy1.render(WINDOW)
            enemy1.resetEnemyBoundaries()

            button1.render(WINDOW)

            # this gets a list of booleans showing which keys are currently pressed
            keysPressed = pygame.key.get_pressed()

            if keysPressed[pygame.K_w]== True:
                player1.movingUp = True

            if keysPressed[pygame.K_s]== True and player1.bottomBound < HEIGHT:
                player1.movingDown = True
            
            if keysPressed[pygame.K_d]== True and player1.rightBound < WIDTH :
                player1.movingRight = True

            if keysPressed[pygame.K_a]== True:
                player1.movingLeft = True

            if keysPressed[pygame.K_w]== False:
                player1.movingUp = False

            if keysPressed[pygame.K_s]== False or player1.bottomBound >= HEIGHT:
                player1.movingDown = False
            
            if keysPressed[pygame.K_d]== False or player1.rightBound >= WIDTH:
                player1.movingRight = False

            if keysPressed[pygame.K_a]== False:
                player1.movingLeft = False
            if button1.isInButton():
                button2 = Button( 100, 100, 50, 50, (255, 0, 255), "world")
                button2.render(WINDOW)
                print("button 2")

            enemy1.ease(player1.x, player1.y)
            
            enemy1.enemyHit(player1)

            #pygame.Rect.colliderect(player1, enemy1)
                       
            pygame.display.update()

        if state == 2: #instructions
            pass
        if state == 3: #credits 
            pass
        if state == 4: #win screen
            pass
        if state == 5: #lose screen
            pass

main()
