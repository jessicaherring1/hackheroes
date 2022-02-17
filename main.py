import pygame
from Player import Player
from Enemy import Enemy 
from Button import Button
from Spritesheet import spritesheet

# Define the size of the game window
WIDTH = 800
HEIGHT = 530

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

#enemyList = []

enemyClock = pygame.time.Clock

timeSince = 5000

enemySprite = spritesheet('enemyRunRight.png')

enemyImages=[]
enemyImages = enemySprite.load_strip((0, 0, 150, 150), 8)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # make the game window object

bg = pygame.image.load("background.jpg").convert()



pygame.display.set_caption("Hackheroes") # name the game window

FPS=60 # frames per second

player1= Player(200, 100)
enemy1 = Enemy(500, 500)
button1 = Button( 50, 50, 100, 50, (255, 0, 0), "hello")



state = 4 #change to 0 at end

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

        if state == 1: #credits
            pass

        if state == 2: #woman instructions
            pass

        if state == 3: #man instructions  
            pass

        if state == 4: #woman (player1) game
            player1.render(WINDOW)
            player1.move()
            player1.resetBoundaries()
            enemy1.render(WINDOW)
            enemy1.resetEnemyBoundaries()

            WINDOW.blit(enemyImages[0], (50, 50))

            # button1.render(WINDOW)
            keyPressed(player1)

            # if button1.isInButton():
            #     button2 = Button( 100, 100, 50, 50, (255, 0, 255), "world")
            #     button2.render(WINDOW)
            #     print("button 2")

            enemy1.ease(player1.x, player1.y)
            
            enemy1.enemyHit(player1)

            #pygame.Rect.colliderect(player1, enemy1)
                       
            pygame.display.update()

            # timeSinceLastSpawn = 0
            # dt = enemyClock.tick()
            # timeSinceLastSpawn += dt
            # if timeSinceLastSpawn > timeSince:
            #      enemyList.append(Enemy( 100, 100)) 
            # timeSinceLastSpawn = 0

        if state == 5: #man (player2) game
            pass

        if state == 6: #win screen woman
            pass

        if state == 7: #win screen man
            pass

        if state == 8: #lose screen woman
            pass

        if state == 9: #lose screen man
            pass

def keyPressed(player):
    keysPressed = pygame.key.get_pressed()

    if keysPressed[pygame.K_w]== True:
        player.movingUp = True

    if keysPressed[pygame.K_s]== True and player.bottomBound < HEIGHT:
        player.movingDown = True
    
    if keysPressed[pygame.K_d]== True and player.rightBound < WIDTH :
        player.movingRight = True

    if keysPressed[pygame.K_a]== True:
        player.movingLeft = True

    if keysPressed[pygame.K_w]== False:
        player.movingUp = False

    if keysPressed[pygame.K_s]== False or player.bottomBound >= HEIGHT:
        player.movingDown = False
    
    if keysPressed[pygame.K_d]== False or player.rightBound >= WIDTH:
        player.movingRight = False

    if keysPressed[pygame.K_a]== False:
        player.movingLeft = False

main()
