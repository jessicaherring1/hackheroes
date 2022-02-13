# button
import pygame
#from pynput.mouse import Button, Controller

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

#def isBetween(aVal, firstBound, secondBound):
#    return (aVal>= firstBound and aVal <= secondBound)

def isInButton(self):
    #mousePressed = pygame.mouse.get_pressed()
  #  if mousePressed:
  return (pygame.mouse.get_pressed()[0] and self.button.collidePoint(pygame.mouse.get_pos()))
        

  
