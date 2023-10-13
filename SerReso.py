import multiprocessing
import socket
import threading
import maingame

IP = "192.168.116.212" #CHANGE IP HERE


# functions ========================

#initialise Server
def StartServeur(ipNb):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((f"{ipNb}", 1234))
    server_socket.listen()
    return server_socket
    
# listen to new player connexions and lauch listening thread
def ConnectJoueur(server_socket,clienListe,clientrequest):
    while len(clienListe) < 4: #max 4 player
       client_socket1, client_addr1 = server_socket.accept()
       clienListe.append((client_socket1, client_addr1))
       print(f"New connection from {client_addr1} to J{len(clienListe)}")
       sendTo(client_socket1,str(len(clienListe)))

       threading.Thread(group=None, target=recoitTout, args=(server_socket,client_socket1,len(clienListe),clientrequest)).start()

# closing server
def ServeurClose(server_socket):
    server_socket.close()

#listening packet from client
def recoitTout(server_socket,client,id,clientrequest):
    while True:
        data = ""
        data = client.recv(1024)
        if len(data) == 0:
            print(f"J{id} déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        elif data.decode("utf-8", errors="ignore")[0:4]=="scan":
            scan =""
            for i in range(len(clienListe)):
                scan += str(clienListe[i][1])+"/"
            scan += "#"
            sendTo(client,scan)
        else :
            clientrequest[id-1] = str(data.decode("utf-8", errors="ignore"))[0:2]
            if clientrequest[id-1]=="re":
                if id==1:
                    ready[0] =True
                elif id ==2:
                    ready[1]=True
                elif id==3:
                    ready[2]=True
                elif id ==4:
                    ready[3]=True
            reception.put(clientrequest)

#send a mesage to all players
def sendAll(clienListe, message):
        
    for i in range(len(clienListe) ):
           #print(i)
           #print(clienListe[i][0])
           try:
                clienListe[i][0].send(message.encode())
           except:
                print(f"erreur send to J{i+1}")
                break

#send a message to a particular client
def sendTo(client_socket,message):
    client_socket.send(message.encode())

#return actual position on game board
def direction_to_XY(direction,oldx,oldy):
    newx = oldx
    newy = oldy
    if direction =="+x" and newx<= 34:
        newy +=1
    elif direction =="-x"and newx>= 1:
        newy-=1
    elif direction =="+y"and newy<= 34:
        newx +=1
    elif direction =="-y"and newy>= 1:
        newx-=1
    return newx,newy

#optional main =============================

if __name__ == "__main__":

    # multithreading variable initialisation
    manager = multiprocessing.Manager()
    clienListe = manager.list() #une liste de tuple avec en [0]sck client [1]ip

    reception = multiprocessing.Queue()
    clientrequest = multiprocessing.Manager().list()
    clientrequest =["+y","+x","-y","-x"] # une lise des longueure 4 contenant les reponses de chaque joueur [0]j1 [1]j2 [2]j3 [3]j4

    board = maingame.initialisation()
    startPointJ1=(17,1)
    startPointJ2=(1,17)
    startPointJ3=(17,35-2)
    startPointJ4=(35-2,17)

    y1,x1 = startPointJ1
    y2,x2 = startPointJ2
    y3,x3 = startPointJ3
    y4,x4 = startPointJ4

    dead1 = False
    dead2 = False
    dead3= False
    dead4 = False

    manager2 = multiprocessing.Manager()
    ready = manager2.list()
    ready =[False,False,False,False]

    #starting server and thread of player connexion
    serveurSocket = StartServeur(IP)
    threading.Thread(group=None, target=ConnectJoueur, args=(serveurSocket,clienListe,clientrequest)).start() 

    while True:
        reponse =""
        if reception.empty()==False :
            retour = reception.get()
            print(retour)
            if all(i==True for i in ready):

                #test if player 1 dead
                if maingame.jouer(1,x1,y1,board,dead1):
                    reponse += str(retour[0])+"/"
                    x1,y1 = direction_to_XY(retour[0],x1,y1)
                else:
                    reponse += str(-1)+"/"
                    board =maingame.erase(1,board)
                    dead1=True
                    print("\n\n\n=====================\n mort j1")

                #test if player 2 dead
                if maingame.jouer(2,x2,y2,board,dead2):
                    reponse += str(retour[1])+"/"
                    x2,y2 = direction_to_XY(retour[1],x2,y2)
                else:
                    reponse += str(-1)+"/"
                    board =maingame.erase(2,board)
                    dead2=True
                    print("\n\n\n=====================\n mort j2")

                #test if player 3 dead
                if maingame.jouer(3,x3,y3,board,dead3):
                    reponse += str(retour[2])+"/"
                    x3,y3 = direction_to_XY(retour[2],x3,y3)
                else:
                    reponse += str(-1)+"/"
                    board =maingame.erase(3,board)
                    dead3=True
                    print("\n\n\n=====================\n mort j3")

                #test if player 4 dead
                if maingame.jouer(4,x4,y4,board,dead4):
                    reponse += str(retour[3])+"/"
                    x4,y4 = direction_to_XY(retour[3],x4,y4)
                else:
                    reponse += str(-1)+"/"
                    board = maingame.erase(4,board)
                    dead4=True
                    print("\n\n\n=====================\n mort j4")

                #send new position to all player               
                sendAll(clienListe,reponse)
                #maingame.affichage(board)
        
        
        
        
    ServeurClose(serveurSocket)
            
            




