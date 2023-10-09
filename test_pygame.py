
import pygame 
from pygame.locals import *

# initializing imported module 
pygame.init() 
  
# displaying a window of height 
# 500 and width 400 
surface = pygame.display.set_mode((1500, 1000)) 

# Initializing RGB Color
bkg = (150,150,150)
mainc=(40, 40, 40)

surface.fill(bkg)

   
# Drawing Rectangle
pygame.draw.rect(surface, mainc,pygame.Rect(10, 10, 1480, 980))

'''fond=pygame.image.load("./image/background.jpg").convert()
fond=pygame.transform.scale(fond,(1480,980))
surface.blit(fond,(10,10))'''

 
# Changing surface color
pygame.display.flip()
  
# creating a bool value which checks 
# if game is running 
running = True
  
# keep game running till running is true 
while running: 
      
    # Check for event if user has pushed 
    # any event in queue 
    for event in pygame.event.get(): 
          
        # if event is of type quit then  
        # set running bool to false 
        if event.type == pygame.QUIT: 
        
            if event.key == K_RIGHT:
                print("droite")
            if event.key == K_LEFT:
                print("gauche")