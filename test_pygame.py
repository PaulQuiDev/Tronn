
import pygame 
from pygame.locals import *
import sys
import maingame

# initializing imported module, clock and colors
pygame.init() 
clock = pygame.time.Clock()
color =(0,0,0)
start=(0,0)
bkg = (150,150,150)
mainc=(40, 40, 40)
line=(200,200,255)
  
# displaying a window and background
surface = pygame.display.set_mode((1505, 1010)) 
surface.fill(bkg)

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# function : initialize start players position
def debut(player):
    
    if player==1:
        color=(255,0,0)
        start = (int(1485*maingame.startPointJ1[0]/33)-5,int(990*maingame.startPointJ1[1]/33))
        startF= (start[0]-5,start[1]-5)

    if player == 2 :
        color =(0,255,0)
        start= (int(1485*maingame.startPointJ2[0]/33),int(990*maingame.startPointJ2[1]/33)+5)
        startF= (start[0]-5,start[1]-5)

    if player == 3:
        color =(255,255,0)
        start = (int(1485*maingame.startPointJ3[0]/33)-5,int(990*maingame.startPointJ3[1]/33)+5)
        startF= (start[0]-5,start[1]-2)
        print("initial")

    if player ==4:
        color=(0,0,255)
        start= (int(1485*maingame.startPointJ4[0]/33),int(990*maingame.startPointJ4[1]/33)+5)
        startF= (start[0]-5,start[1]-5)
       
    pygame.draw.rect(surface,color,pygame.Rect((start[0]-10,start[1]-10),(10,10)))
    pygame.display.flip()
  
    return startF, color


#function : mouve one player in a specified direction
def avancer(player,x,y,direction,color):
    #define numer of pixels for an horizontal (x) or vertical (y) mouve
    xunit = 45
    yunit=30
    if direction =="+x":
        newx= x+xunit
        newy = y
        maingame.affichage(maingame.tab)
    if direction =="-x":
        newx=x-xunit
        newy = y
        maingame.affichage(maingame.tab)
    if direction =="+y":
        newx = x
        newy= y+yunit
        maingame.affichage(maingame.tab)
    if direction =="-y":
        newx=x
        newy=y-yunit
        maingame.affichage(maingame.tab)

    #bloc the line in the window
    if newx>1495:
        newx=1495
    elif newx<10 :
        newx =10
    if newy >1000:
        newy=1000
    elif newy<10:
        newy=10

    #draw mouve
    pygame.draw.line(surface,color,(x,y),(newx,newy),width=5)
    pygame.display.flip()
    return newx,newy # return new current position

#function: define new direction acording to the current direction
def changementDir (old,newdir):
    new="+y"
    if old=="+y":
        if newdir =='D':
            new ="+x"
        elif newdir=='G':
            new="-x"
    elif old=="-y":
        if newdir =='D':
            new ="+x"
        elif newdir=='G':
            new="-x"
    elif old=="+x":
        if newdir =='H':
            new ="-y"
        elif newdir=='B':
            new="+y"
    elif old=="-x":
        if newdir =='H':
            new ="-y"
        elif newdir=='B':
            new="+y"

    return new

#function : convert a pixel position in an integer index
def Xconvert_px_to_index(xpx):
    if player==3:
        x=int(xpx*33/1485)
    else:
        x=int(xpx*33/1485)+1
    return x
def Yconvert_px_to_index(ypx):
    if player==3:
        y=int(ypx*33/990)
    else:
        y=int(ypx*33/990)+1
    return y

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   
# Drawing background grid
pygame.draw.rect(surface, mainc,pygame.Rect(10, 10, 1485, 990))
for i in range(10,1485,45):
    pygame.draw.line(surface,line,(i,10),(i,1000))
pygame.draw.line(surface,line,(1495,10),(1495,1000))

for i in range(10,991,30):
    pygame.draw.line(surface,line,(10,i),(1495,i))
pygame.draw.line(surface,line,(10,1495),(1000,1495))

pygame.display.flip() #refresh rendering
  

# creat setup variable and initialize game
player=3
start,color = debut(player)
x,y=start
globalDirection = "-y"

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
  
# Game Loop
while True: 

    clock.tick(10) #manage fps rate 

    # Check for event if user has pushed any event
    for event in pygame.event.get():   

        # quit event
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        #user key press event
        if event.type == pygame.KEYDOWN:
            #manage vertical mouve
            if globalDirection=="+y" or globalDirection=="-y":
                if event.key == K_RIGHT:
                    globalDirection=changementDir(globalDirection,"D")
                if event.key == K_LEFT:
                    globalDirection=changementDir(globalDirection,"G")

            #manage horizontal mouve
            elif globalDirection=="+x" or globalDirection=="-x":
                if event.key == K_UP:
                    globalDirection=changementDir(globalDirection,"H")
                if event.key == K_DOWN:
                    globalDirection=changementDir(globalDirection,"B")
    
    # look the save matrix (maingame.tab), if case are free, move forward
    if maingame.jouer(player,Yconvert_px_to_index(y),Xconvert_px_to_index(x), maingame.tab):
        x,y=avancer(player,x,y,globalDirection,color)


        

