
import pygame 
from pygame.locals import *
import sys
import multiprocessing
import CliReso
import maingame
import socket
#initialize = = = = = = = = = = = = = = = = = = = = = = = = 

# initializing imported module, clock and colors
pygame.init() 
clock = pygame.time.Clock()
color =(0,0,0)
start=(0,0)
bkg = (150,150,150)
mainc=(40, 40, 40)
line=(200,200,255)
shadow=(80,80,80)
answer = multiprocessing.Queue()
connecte =[]

# displaying a window and background
surface = pygame.display.set_mode((1505, 1010)) 
surface.fill(bkg)

#Functions = = = = = = = = = = = = = = = = = = = = = = = = 

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
        
    if player ==4:
        color=(0,0,255)
        start= (int(1485*maingame.startPointJ4[0]/33),int(990*maingame.startPointJ4[1]/33)+5)
        startF= (start[0]-5,start[1]-5)
       
    pygame.draw.rect(surface,color,pygame.Rect((start[0]-10,start[1]-10),(10,10)))
    pygame.display.flip()
  
    return startF, color


#function : mouve one player in a specified direction
def avancer(x,y,direction,color):
    #define numer of pixels for an horizontal (x) or vertical (y) mouve
    xunit = 45
    yunit=30
    newx =0
    newy=0

    if direction =="+x":
        newx= x+xunit
        newy = y
        
    if direction =="-x":
        newx=x-xunit
        newy = y
        
    if direction =="+y":
        newx = x
        newy= y+yunit
        
    if direction =="-y":
        newx=x
        newy=y-yunit
        

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
    if playercurrent==3:
        x=int(xpx*33/1485)
    else:
        x=int(xpx*33/1485)+1
    return x
def Yconvert_px_to_index(ypx):
    if playercurrent==3:
        y=int(ypx*33/990)
    else:
        y=int(ypx*33/990)+1
    return y

# fuction : erase a color from window 
def erase(color):
    arr = pygame.PixelArray(surface)
    arr.replace(color, bkg)
    del arr

# Connexion menu = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# affichage du menu de connexion
start = False
sck= CliReso.ConnectionClient(answer) # start connection !

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
text = font.render('Press enter key to Start Game...', True, bkg, mainc)
surface.blit(text, (540,940))
pygame.display.flip()

while True :
    
    if answer.empty() != True:
        CliReso.scanPlayer(sck)
        rep = answer.get().decode("utf-8", errors="ignore")

        #print(nbClient + " recu ")
        nbClient = rep.split("#")
        nbClient = nbClient[0].split("/")
        connecte = nbClient[0:-1]
        #print("connecte = " + str(connecte))
        
    if len(connecte)!=0 and start == False:
        y= 300
        for i in range(len(connecte)):
            textshow = "joueur "+str(i+1)+"  "+connecte[i]+".............................................connect"
            font = pygame.font.SysFont('urwbookman', 15)
            text = font.render(textshow, True, bkg, shadow)
            surface.blit(text, (500,y+i*30))
            pygame.display.flip()

    for event in pygame.event.get():   
        # quit event
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        #user key press event
        if event.type == pygame.KEYDOWN and start==False:
            
            if event.key == K_RETURN:
                start=True
                CliReso.Send("re",sck)
    if start:
        # Drawing background grid
        pygame.draw.rect(surface, mainc,pygame.Rect(10, 10, 1485, 990))
        for i in range(10,1485,45):
            pygame.draw.line(surface,line,(i,10),(i,1000))
        pygame.draw.line(surface,line,(1495,10),(1495,100))
        for i in range(10,991,30):
            pygame.draw.line(surface,line,(10,i),(1495,i))
        pygame.display.flip() #refresh rendering 
        break


 
# create, setup variable and initialize game = = = = = = = = = = = = = = = = = = = = = = = = = =
print(rep)
rep=rep
rep = rep[0:-2]
rep_split = rep.split('/')
compare=[]
print(rep_split)
for i in range(len(rep_split)):
    part= rep_split[i].split(',')
    compare.append( part[1][1:-1])

playercurrent = 1
for i in range(len(compare)):
    print(compare[i])
    print(sck.getsockname()[1])
    if int(compare[i])== int(sck.getsockname()[1]) :
        playercurrent = (i+1)
        break
print(f"you are J{playercurrent}")
if playercurrent == 1 :
    direction_current="+y"
elif playercurrent ==2 :
    direction_current="+x"
elif playercurrent ==3 :
    direction_current="-y"
elif playercurrent == 4 :
    direction_current="-x"



start1,color1 = debut(1)
x1,y1=start1
globalDirection = "+y"

start2,color2 = debut(2)
x2,y2=start2
gD2 = "+x"

start3,color3 = debut(3)
x3,y3=start3
gD3 = "-y"

start4,color4 = debut(4)
x4,y4=start4
gD4 = "-x"

dead = False

while answer.empty():
    try :
        print(answer.get())
    except:
        print('fini')
#Game Loop = = = = = = = = = = = = = = = = = = = = = = = = = =

while start: 
    clock.tick(3) #manage fps rate 

    # Check for event if user has pushed any event
    for event in pygame.event.get():   

        # quit event
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        #user key press event
        if event.type == pygame.KEYDOWN:
            
            #manage vertical mouve
            if direction_current=="+y" or direction_current=="-y":
                if event.key == K_RIGHT:
                    direction_current=changementDir(direction_current,"D")
                if event.key == K_LEFT:
                    direction_current=changementDir(direction_current,"G")
            #manage horizontal mouve
            elif direction_current=="+x" or direction_current=="-x":
                if event.key == K_UP:
                    direction_current=changementDir(direction_current,"H")
                if event.key == K_DOWN:
                    direction_current=changementDir(direction_current,"B")
    
    # send new direction to server if player is not dead
    if sck!="E" and dead==False:
        CliReso.Send(direction_current,sck)
    
    # read answer queue from server and updat directions
    if answer.empty()==False:
        update= answer.get()
        update = update.decode("utf-8",errors = "ignore")
        up_split = update.split('/')
        globalDirection = up_split[0]
        gD2= up_split[1]
        gD3 = up_split[2]
        gD4 = up_split[3]

        #move player if he's not dead
        if globalDirection == "-1" or dead:
            erase(color1)
            pygame.display.flip()
            if playercurrent ==1:
                dead=True
        else:
            x1,y1=avancer(x1,y1,globalDirection,color1)

        if gD2 =="-1" or dead:
            erase(color2)
            pygame.display.flip()
            if playercurrent ==2:
                dead=True
        else :
            x2,y2=avancer(x2,y2,gD2,color2)

        if gD3 == "-1" or dead:
            erase(color3)
            pygame.display.flip()
            if playercurrent ==3:
                dead=True
        else : 
            x3,y3=avancer(x3,y3,gD3,color3)

        if gD4 =="-1" or dead:
            erase(color4)
            pygame.display.flip()
            if playercurrent ==4:
                dead=True
        else :
            x4,y4=avancer(x4,y4,gD4,color4)
        

            

