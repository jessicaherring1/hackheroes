# button
import pygame
pygame.font.init()
#from pynput.mouse import Button, Controller

class Button:
    

    def __init__(self, tempX, tempY, tempW, tempH, tempColor, tempText):
            self.x = tempX #x location of button
            self.y = tempY #y location of button
            self.w = tempW #width of button
            self.h = tempH #height of button
            self.color = tempColor #color of button
            self.text = tempText #text on button

    def render(self, aSurface):
        self.button = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(aSurface, self.color, self.button)

        myFont = pygame.font.SysFont('Calibri', 20, True, False)
        text = myFont.render(self.text, True, (0, 0, 0))
        aSurface.blit(text, [250, 250])

    #def isBetween(aVal, firstBound, secondBound):
    #    return (aVal>= firstBound and aVal <= secondBound)

    def isInButton(self):
        #mousePressed = pygame.mouse.get_pressed()
    #  if mousePressed:
        pygame.event.get()
        return (pygame.mouse.get_pressed()[0] and self.button.collidepoint(pygame.mouse.get_pos()))
            

  
