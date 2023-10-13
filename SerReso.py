import multiprocessing
import socket
import threading
import maingame
import time


# les imports =====================================



# initialisation truc important ========================

def StartServeur(ipNb):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((f"{ipNb}", 8888))
    server_socket.listen()
    return server_socket
    

def ConnectJoueur(server_socket,clienListe,clientrequest):
    while len(clienListe) < 4:
       client_socket1, client_addr1 = server_socket.accept()
       clienListe.append((client_socket1, client_addr1))
       print(f"New connection from {client_addr1} to J{len(clienListe)}")
       threading.Thread(group=None, target=recoitTout, args=(server_socket,client_socket1,len(clienListe),clientrequest)).start()


def ServeurClose(server_socket):
    server_socket.close()


'''def recoit(server_socket,client_socket):# connection privilégier de J1
    while True:
        # or 'with lock:' (instead of acquire and release)
        data = client_socket.recv(1024)
        if len(data) == 0:
            print("J1 déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        #queuJ1.put(str(data)[2:-1])
        print(str(data)[2:-1])'''


def recoitTout(server_socket,client,id,clientrequest):
    #data2= ""
    while True:
        data = ""
        data = client.recv(1024)
        if len(data) == 0:
            print(f"J{id} déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        #print(f"J{id}:{str(data)[2:-1]}")
        #if data != data2 :
        clientrequest[id-1] = str(data.decode("utf-8", errors="ignore"))[0:2]
        #print(str(id-1) + " " + str(data)[2:4])
        reception.put(clientrequest)
        #data2=data




'''def connect(server_socket):
    while True:
        if len(clienListe) < 4:
            client_socket1, client_addr1 = server_socket.accept()
            clienListe.append((client_socket1, client_addr1))
            print(f"New connection from {client_addr1} to J{len(clienListe)}")
            threading.Thread(group=None, target=recoitTout, args=(server_socket,client_socket1,len(clienListe))).start()'''


def sendAll(clienListe, message):
        
    for i in range(len(clienListe) ):
           #print(i)
           #print(clienListe[i][0])
           try:
                clienListe[i][0].send(message.encode())
           except:
                print(f"erreur send to J{i+1}")
                break

def sendTo(client_socket,message):
    client_socket.send(message.encode())

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
    #print("old : "+str(oldx)+" "+str(oldy)+" new : "+str(newx)+" "+str(newy))
    return newx,newy

# les definitions =============================



if __name__ == "__main__":
    manager = multiprocessing.Manager()
    #page d'accueil
    clienListe = manager.list() #une liste de tuple avec en [0]sck client [1]ip

    reception = multiprocessing.Queue()
    #tour de jeu
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

    serveurSocket = StartServeur("127.0.0.1")
    threading.Thread(group=None, target=ConnectJoueur, args=(serveurSocket,clienListe,clientrequest)).start() 
    #lancer fonction connectJoueur()
    
    while True:
       
        reponse =""
        #time.sleep(0.1)
        if reception.empty()==False :
            retour = reception.get()

            if maingame.jouer(1,x1,y1,board,dead1):
                reponse += str(retour[0])+"/"
                x1,y1 = direction_to_XY(retour[0],x1,y1)
            else:
                reponse += str(-1)+"/"
                board =maingame.erase(1,board)
                dead1=True
                print("\n\n\n=====================\n mort j1")

            if maingame.jouer(2,x2,y2,board,dead2):
                reponse += str(retour[1])+"/"
                x2,y2 = direction_to_XY(retour[1],x2,y2)
            else:
                reponse += str(-1)+"/"
                board =maingame.erase(2,board)
                dead2=True
                print("\n\n\n=====================\n mort j2")

            if maingame.jouer(3,x3,y3,board,dead3):
                reponse += str(retour[2])+"/"
                x3,y3 = direction_to_XY(retour[2],x3,y3)
            else:
                reponse += str(-1)+"/"
                board =maingame.erase(3,board)
                dead3=True
                print("\n\n\n=====================\n mort j3")

            if maingame.jouer(4,x4,y4,board,dead4):
                reponse += str(retour[3])+"/"
                x4,y4 = direction_to_XY(retour[3],x4,y4)
            else:
                reponse += str(-1)+"/"
                board = maingame.erase(4,board)
                dead4=True
                print("\n\n\n=====================\n mort j4")
                            
            sendAll(clienListe,reponse)
            maingame.affichage(board)
    
    
    
    
    ServeurClose(serveurSocket)
        
        




