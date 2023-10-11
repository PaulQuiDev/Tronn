import multiprocessing
import socket
import threading

# les imports =====================================

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen()
# 1er étape
manager = multiprocessing.Manager()
clienListe = manager.list()


# initialisation truc important ========================

def SarteServeur():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8888))
    server_socket.listen()




def recoit():# connection privilégier de J1
    while True:
        # or 'with lock:' (instead of acquire and release)
        data = client_socket.recv(1024)
        if len(data) == 0:
            print("J1 déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        #queuJ1.put(str(data)[2:-1])
        print(str(data)[2:-1])


def recoitTout(client,id):
    while True:
        # or 'with lock:' (instead of acquire and release)
        #print("reception")
        data = client.recv(1024)
        if len(data) == 0:
            print(f"J{id} déconnecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        print(f"J{id}:{str(data)[2:-1]}")


def connect():
    while True:
        if len(clienListe) < 4:
            client_socket1, client_addr1 = server_socket.accept()
            clienListe.append((client_socket1, client_addr1))
            print(f"New connection from {client_addr1} to J{len(clienListe)}")
            threading.Thread(group=None, target=recoitTout, args=(client_socket1,len(clienListe))).start()


def sendAll():
    s = input()
    client_socket.send(s.encode())
    if s[0] == "A":
        s= s[1:]
        try:
            for i in range(len(clienListe) - 1):
                clienListe[i + 1][0].send(s.encode())

        except:
            print("erreur send")

# les definitions =============================


#  = = = = = = = = = = = = = = = = = == = = = = =
client_socket, client_addr = server_socket.accept()
print(f"New connection from {client_addr} to J1")


clienListe.append((client_socket, client_addr))

thrconect = threading.Thread(group=None, target=recoit)
thrconect.start()


thrlien = threading.Thread(group=None, target=connect)
thrlien.start()


# connecter = = = = = =  = = = = = = = = = = =


#while True:
 #   s = input()
  #  client_socket.send(s.encode())
   # if s[0] == "A":
    #    try:
     #       for i in range(len(clienListe) - 1):
      #          clienListe[i + 1][0].send(s.encode())
#
 #       except:
  #          print("erreur send")
   # if s[0] == 'B':
    #    print(queuJ1.get())
