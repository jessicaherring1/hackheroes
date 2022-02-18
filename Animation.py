import pygame


class Animation:
    # variables
    index = 0
    isAnimating = False

    def __init__(self, tempImages, tempSpeed, tempScale):
        self.Images = tempImages
        self.speed = tempSpeed
        self.scale = tempScale

  # updates the index which image to display for
  # the animation

    def next(self):
        print(self.index)
        self.index += self.speed

        # resets the index if it is too big
        if (self.index >= len(self.Images)):
            self.index = 0
            self.isAnimating = False

    # display an image of the animation

    def display(self, x, y, aSurface):
        if (self.isAnimating):
            imageIndex = int (self.index)
            img = self.Images[imageIndex]
            aSurface.blit(img, (x, y))

            #increment the index of the images to display
            self.next()
        else :
            img = self.Images[0]
            aSurface.blit(img, (x, y))
