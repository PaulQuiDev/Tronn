import pygame
import sys

def Start():

    pygame.init()
    bkg = (250,250,250)

    surface = pygame.display.set_mode((1505, 1010)) 
    surface.fill(bkg)
    mainc=(40, 40, 40)
    pygame.draw.rect(surface, mainc,pygame.Rect(10, 210, 1485, 790))
    pygame.draw.rect(surface, mainc,pygame.Rect(20, 20, 1465, 170))
    pygame.display.flip()

    #print(pygame.font.get_fonts())
    font = pygame.font.SysFont('urwbookman', 52)
    text = font.render('Welcome in Tron Game !', True, bkg, mainc)
    surface.blit(text, (450,80))
    pygame.display.flip()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                surface.fill((0,0,0))
                pygame.display.flip()

            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit() 
    

Start()