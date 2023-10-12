import pygame
import sys

def Start():

    #definition des variables 

    pygame.init()
    bkg = (250,250,250)
    mainc=(40, 40, 40)
    shadow=(80,80,80)
    connecté =[]#("client socket","001.0235.2359.002"),("client socket","001.0235.2359.002"),("client socket","001.0235.2359.002")]

    #affichage du fond 

    surface = pygame.display.set_mode((1505, 1010)) 
    surface.fill(bkg)
    
    pygame.draw.rect(surface, mainc,pygame.Rect(10, 210, 1485, 790))
    pygame.draw.rect(surface, mainc,pygame.Rect(20, 20, 1465, 170))

    #affichage du titre

    font = pygame.font.SysFont('urwbookman', 52)
    text = font.render('Welcome in Tron Game !', True, bkg, mainc)
    surface.blit(text, (450,80))


    pygame.draw.rect(surface,shadow,pygame.Rect(450,250,650,650))
    pygame.display.flip()

    # affichage de la consigne
    font = pygame.font.SysFont('urwbookman', 30)
    text = font.render('Press any key to Start Game...', True, bkg, mainc)
    surface.blit(text, (540,940))
    pygame.display.flip()
    
    
    while True:

        '''  time.sleep(0.5)
        pygame.draw.rect(surface,mainc,pygame.Rect(540,940,650,40))
        pygame.display.flip()
        time.sleep(0.5)'''

        # affichage des client connecté en temps réel
        if len(connecté)!=0:
            y= 300
            for i in range(len(connecté)):
                textshow = "joueur "+str(i+1)+"  "+connecté[i][1]+".............................................connect"
                font = pygame.font.SysFont('urwbookman', 15)
                text = font.render(textshow, True, bkg, shadow)
                surface.blit(text, (500,y+i*30))
                pygame.display.flip()
        
        #changement d'affichage au lancement du jeu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                surface.fill((0,0,0))
                pygame.display.flip()
            
            # quite pygame
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit() 

Start()