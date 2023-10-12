import multiprocessing
import socket
import threading

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
    data2= ""
    while True:
        data = client.recv(1024)
        if len(data) == 0:
            print(f"J{id} déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        #print(f"J{id}:{str(data)[2:-1]}")
        if data != data2 :
            clientrequest[id-1] = str(data)[2:4]
            data2=data


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
                print(f"erreur send to J{i}")

def sendTo(client_socket,message):
    client_socket.send(message.encode())


# les definitions =============================



if __name__ == "__main__":
    manager = multiprocessing.Manager()
    #page d'accueil
    clienListe = manager.list() #une liste de tuple avec en [0]sck client [1]ip

    #tour de jeu
    clientrequest = multiprocessing.Manager().list()
    clientrequest.extend(range(4)) # une lise des longueure 4 contenant les reponses de chaque joueur [0]j1 [1]j2 [2]j3 [3]j4

    serveurSocket = StartServeur("127.0.0.1")
    threading.Thread(group=None, target=ConnectJoueur, args=(serveurSocket,clienListe,clientrequest)).start() 
    #lancer fonction connectJoueur()
    while True:
        s = input()
        print(clientrequest)
    
    ServeurClose(serveurSocket)
        
        




