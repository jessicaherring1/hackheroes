from operator import truediv
import pygame
from Animation import Animation
from Player import Player
from Enemy import Enemy 
from Button import Button
from Spritesheet import spritesheet
import random

# Define the size of the game window
WIDTH = 800
HEIGHT = 530

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)


enemyClock = pygame.time.Clock()

# timeSince = 5000

totalSpawnEnemies = 10

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # make the game window object

bg = pygame.image.load("background.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))



pygame.display.set_caption("Hackheroes") # name the game window

FPS=60 # frames per second

player1= Player(200, 100)
# enemy1 = Enemy(500, 500)
button1 = Button( 50, 50, 100, 50, (255, 0, 0), "hello")



state = 4 #change to 0 at end

# ANIMATION STUFF!!!!!!!!
#regular guy 
guyWalkingRightSprite = spritesheet('guyWalkingRight.png')
guyWalkingRightImages=[]
guyWalkingRightImages = guyWalkingRightSprite.load_strip((0, 0, 15, 32), 4)
guyWalkingRight = Animation(guyWalkingRightImages, 0.2, 1.5)

guyWalkingLeftSprite = spritesheet('guyWalkingLeft.png')
guyWalkingLeftImages=[]
guyWalkingLeftImages = guyWalkingLeftSprite.load_strip((0, 0, 15, 32), 4)
guyWalkingLeft = Animation(guyWalkingLeftImages, 0.2, 1.5)


#enemy
enemyRunRightSprite = spritesheet('enemyRunRight.png')
enemyRunRightImages=[]
enemyRunRightImages = enemyRunRightSprite.load_strip((0, 0, 150, 150), 8)
enemyRunRight = Animation(enemyRunRightImages, 0.2, 2)

enemyRunLeftSprite = spritesheet('enemyRunLeft.png')
enemyRunLeftImages=[]
enemyRunLeftImages = enemyRunLeftSprite.load_strip((0, 0, 150, 150), 8)
enemyRunLeft= Animation(enemyRunLeftImages, 0.2, 2)

enemyDeathRightSprite = spritesheet('enemyDeathRight.png')
enemyDeathRightImages=[]
enemyDeathRightImages = enemyDeathRightSprite.load_strip((0, 0, 150, 150), 4)
enemyDeathRight= Animation(enemyDeathRightImages, 0.2, 2)

enemyDeathLeftSprite = spritesheet('enemyDeathLeft.png')
enemyDeathLeftImages=[]
enemyDeathLeftImages = enemyDeathLeftSprite.load_strip((0, 0, 150, 150), 4)
enemyDeathLeft= Animation(enemyDeathLeftImages, 0.2, 2)

enemyAttackRightSprite = spritesheet('enemyAttackRight.png')
enemyAttackRightImages=[]
enemyAttackRightImages = enemyAttackRightSprite.load_strip((0, 0, 150, 150), 8)
enemyAttackRight= Animation(enemyAttackRightImages, 0.2, 2)

enemyAttackLeftSprite = spritesheet('enemyAttackLeft.png')
enemyAttackLeftImages=[]
enemyAttackLeftImages = enemyAttackLeftSprite.load_strip((0, 0, 150, 150), 8)
enemyAttackLeft= Animation(enemyAttackLeftImages, 0.2, 2)

enemyIdleSprite = spritesheet('enemyIdle.png')
enemyIdleImages=[]
enemyIdleImages = enemyIdleSprite.load_strip((0, 0, 150, 150), 4)
enemyIdle= Animation(enemyIdleImages, 0.2, 2)

#player 2 (man)
player2RunRightSprite = spritesheet('player2RunRight.png')
player2RunRightImages=[]
player2RunRightImages = player2RunRightSprite.load_strip((0, 0, 100, 100), 8)
player2RunRight = Animation(player2RunRightImages, 0.2, 2)

player2RunLeftSprite = spritesheet('player2RunLeft.png')
player2RunLeftImages=[]
player2RunLeftImages = player2RunLeftSprite.load_strip((0, 0, 100, 100), 8)
player2RunLeft= Animation(player2RunLeftImages, 0.2, 2)

player2DeathRightSprite = spritesheet('player2DeathRight.png')
player2DeathRightImages=[]
player2DeathRightImages = player2DeathRightSprite.load_strip((0, 0, 100, 100), 4)
player2DeathRight= Animation(player2DeathRightImages, 0.2, 2)

player2DeathLeftSprite = spritesheet('player2DeathLeft.png')
player2DeathLeftImages=[]
player2DeathLeftImages = player2DeathLeftSprite.load_strip((0, 0, 100, 100), 4)
player2DeathLeft= Animation(player2DeathLeftImages, 0.2, 2)

player2AttackRightSprite = spritesheet('player2AttackRight.png')
player2AttackRightImages=[]
player2AttackRightImages = player2AttackRightSprite.load_strip((0, 0, 100, 100), 4)
player2AttackRight= Animation(player2AttackRightImages, 0.2, 2)

player2AttackLeftSprite = spritesheet('player2AttackLeft.png')
player2AttackLeftImages=[]
player2AttackLeftImages = player2AttackLeftSprite.load_strip((0, 0, 100, 100), 4)
player2AttackLeft= Animation(player2AttackLeftImages, 0.2, 2)

player2IdleSprite = spritesheet('player2Idle.png')
player2IdleImages=[]
player2IdleImages = player2IdleSprite.load_strip((0, 0, 100, 100), 4)
player2Idle= Animation(player2IdleImages, 0.2, 2)

#transformation 
transformationSprite = spritesheet('transformation.png')
transformationImages=[]
transformationImages = transformationSprite.load_strip((0, 0, 100, 100), 7)
transformation= Animation(transformationImages, 0.2, 2)

#player 1 (woman)
player1RunRightImages = []
for i in range(1,9):
    img = pygame.image.load("player1RunRight/RR"+str(i)+".png")
    player1RunRightImages.append(img)
player1RunRight = Animation(player1RunRightImages, 0.2, 2.5)


player1RunLeftImages = []
for i in range(1,9):
    img = pygame.image.load("player1RunLeft/RL"+str(i)+".png")
    player1RunLeftImages.append(img)
player1RunLeft = Animation(player1RunLeftImages, 0.2, 2.5)

player1AttackLeftImages = []
for i in range(1,12):
    img = pygame.image.load("player1AttackLeft/AL"+str(i)+".png")
    player1AttackLeftImages.append(img)
player1AttackLeft = Animation(player1AttackLeftImages, 0.2, 2.5)

player1AttackRightImages = []
for i in range(1,12):
    img = pygame.image.load("player1AttackRight/AR"+str(i)+".png")
    player1AttackRightImages.append(img)
player1AttackRight = Animation(player1AttackRightImages, 0.2, 2.5)

player1DeathLeftImages = []
for i in range(1,11):
    img = pygame.image.load("player1DeathLeft/DL"+str(i)+".png")
    player1DeathLeftImages.append(img)
player1DeathLeft = Animation(player1DeathLeftImages, 0.2, 2.5)

player1DeathRightImages = []
for i in range(1,11):
    img = pygame.image.load("player1DeathRight/DR"+str(i)+".png")
    player1DeathRightImages.append(img)
player1DeathRight = Animation(player1DeathRightImages, 0.2, 2.5)

player1IdleImages = []
for i in range(1,6):
    img = pygame.image.load("player1Idle/I"+str(i)+".png")
    player1IdleImages.append(img)
player1Idle = Animation(player1IdleImages, 0.2, 2)

def main():
    clock = pygame.time.Clock()
    enemyClock = pygame.time.Clock()
    numEnemySpawn = 0

    timeSince = 5000
    timeSinceLastSpawn = 0

    running = True #boolean that represents whether the game should continue to run or not

    enemyList = []

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
            # enemy1.render(WINDOW)
            # enemy1.resetEnemyBoundaries()

           # WINDOW.blit(enemyRunRightImages[0], (50, 50))


            # transformation.isAnimating=True
            # transformation.display(100, 100, WINDOW)

            # player1Idle.isAnimating=True
            # player1Idle.display(100, 100, WINDOW)


            # button1.render(WINDOW)
            keyPressed(player1)

            # if button1.isInButton():
            #     button2 = Button( 100, 100, 50, 50, (255, 0, 255), "world")
            #     button2.render(WINDOW)
            #     print("button 2")

            # enemy1.ease(player1.x, player1.y)
            
            # enemy1.enemyHit(player1)

            #pygame.Rect.colliderect(player1, enemy1)
                       
                   
            dt = enemyClock.tick()
            timeSinceLastSpawn += dt
            if timeSinceLastSpawn > timeSince and numEnemySpawn <= totalSpawnEnemies:
                enemyList.append(Enemy(random.randint(0,WIDTH), random.randint(0, HEIGHT))) 
                timeSinceLastSpawn = 0
                numEnemySpawn += 1

        for enemy in enemyList:
            # enemy.render(WINDOW)
            enemy.ease(player1.x, player1.y)
            enemy.resetEnemyBoundaries()
            enemy.enemyHit(player1)
            if enemy.dx >= 0:
                enemyRunRight.isAnimating = True
                enemyRunRight.display(enemy.x, enemy.y, WINDOW)
            if enemy.dx < 0:
                enemyRunLeft.isAnimating = True
                enemyRunLeft.display(enemy.x, enemy.y, WINDOW)
            # if enemy.dy >= 0:
            #     enemyIdle.isAnimating = True
            #     enemyIdle.display(enemy.x, enemy.y, WINDOW)

        # if (numEnemySpawn == 10 and len(enemyList) == 0)
        # win screen time
        pygame.display.update()

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
        player2Idle.isAnimating = True
        player2Idle.display(player.x, player.y, WINDOW)
    else:
        player2Idle.isAnimating = False


    if keysPressed[pygame.K_s]== True and player.bottomBound < HEIGHT:
        player.movingDown = True
        player2Idle.isAnimating = True
        player2Idle.display(player.x, player.y, WINDOW)
    else:
        player2Idle.isAnimating = False
       
    
    if keysPressed[pygame.K_d]== True and player.rightBound < WIDTH :
        player.movingRight = True
        player1RunRight.isAnimating = True
        player1RunRight.display(player.x, player.y, WINDOW)
        player2RunRight.isAnimating = True
        player2RunRight.display(player.x, player.y, WINDOW)
    else:
        player1RunRight.isAnimating = False
        player2RunRight.isAnimating = False
        #add: player1RunRight.isAnimating = True

    if keysPressed[pygame.K_a]== True:
        player.movingLeft = True
        player1RunLeft.isAnimating = True
        player1RunLeft.display(player.x, player.y, WINDOW)
        player2RunLeft.isAnimating = True
        player2RunLeft.display(player.x, player.y, WINDOW)
        #add: player1RunLeft.isAnimating = True
    else:
        player1RunLeft.isAnimating = False 
        player2RunLeft.isAnimating = False 

    if keysPressed[pygame.K_w]== False:
        player.movingUp = False

    if keysPressed[pygame.K_s]== False or player.bottomBound >= HEIGHT:
        player.movingDown = False
    
    if keysPressed[pygame.K_d]== False or player.rightBound >= WIDTH:
        player.movingRight = False

    if keysPressed[pygame.K_a]== False:
        player.movingLeft = False

    if  (not player2RunLeft.isAnimating and not player2RunRight.isAnimating and not 
            player2AttackLeft.isAnimating and not player2AttackRight.isAnimating and not 
            player2DeathLeft.isAnimating and not player2DeathRight.isAnimating):
        player2Idle.isAnimating = True
        player2Idle.display(player.x, player.y, WINDOW)
    else:
        player2Idle.isAnimating = False

    if  (not player1RunLeft.isAnimating and not player1RunRight.isAnimating and not 
            player1AttackLeft.isAnimating and not player1AttackRight.isAnimating and not 
            player1DeathLeft.isAnimating and not player1DeathRight.isAnimating):
        player1Idle.isAnimating = True
        player1Idle.display(player.x, player.y, WINDOW)
    else:
        player1Idle.isAnimating = False

main()
