import pygame, sys
from pygame.locals import *
import time


pygame.init()

#set up the Window
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("DOG ANIMATION :)")

#define colors
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

#define the cat image

dog = pygame.image.load("dog.png")
scaledog = pygame.transform.scale(dog,(80,80))
dogx = 10
dogy = 10
direction = "right"

#define the title font objects
fontObj = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj = fontObj.render("Animation - Part 1", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150) #the coordinate for the text

while True: #the main game loop
    DISPLAYSURF.fill(WHITE)

    #write the heading
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    if direction == "right":
        dogx += 5
        if dogx == 280:
            direction = "down"
        elif direction == "left":
            dogx -= 5   
            if dogx == 10:
                direction = "right"
        elif direction == "down":
          dogy -= 5
          if dogy == 10:
            direction = "up"
        elif direction == "up":
          dogy += 5
          if dogy == 280:
            direction = "down"

    #draw the image at point (x, y)
    DISPLAYSURF.blit(dog, (dogx, dogy)) #draws image at (10,10)
    DISPLAYSURF.blit(scaledog,(dogx, dogy))
    time.sleep(0.025)

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()



