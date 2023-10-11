import multiprocessing
import socket
import threading

# les importes =====================================

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen()


lock = threading.Lock()  # ?

# initialisation truc importent ========================


def resoit():# conetion privilégier de J1
    while True:
        # or 'with lock:' (instead of acquire and release)
        data = client_socket.recv(1024)
        if len(data) == 0:
            print("J1 déconecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        print(data)


def resoitTout(client,id):
    while True:
        # or 'with lock:' (instead of acquire and release)
        #print("reception")
        data = client.recv(1024)
        if len(data) == 0:
            print(f"J{id} déconecter ¯\_(ツ)_/¯")
            server_socket.close()
            break
        print(f"J{id}:{str(data)[2:-1]}")


def connect():
    while True:
        if len(clienListe) < 4:
            client_socket1, client_addr1 = server_socket.accept()
            clienListe.append((client_socket1, client_addr1))
            print(f"New connection from {client_addr1} to J{len(clienListe)}")
            threading.Thread(group=None, target=resoitTout, args=(client_socket1,len(clienListe))).start()


def sendAll():
    s = input()
    client_socket.send(s.encode())
    if s[0] == "A":
        s= s[1:] #retirer le A
        try:
            for i in range(len(clienListe) - 1):
                clienListe[i + 1][0].send(s.encode())

        except:
            print("erreur send")

# les definition =============================


#  = = = = = = = = = = = = = = = = = == = = = = =
client_socket, client_addr = server_socket.accept()
print(f"New connection from {client_addr} to J1")

clienListe = []
clienListe.append((client_socket, client_addr))
# print(clienListe[0][1]) # premier clie puis clien adresse
# print(len(clienListe)) sa marche

thrconect = threading.Thread(group=None, target=resoit)
thrconect.start()

thrlien = threading.Thread(group=None, target=connect)
thrlien.start()


# conecter = = = = = =  = = = = = = = = = = =


while True:
    s = input()
    client_socket.send(s.encode())
    if s[0] == "A":
        try:
            for i in range(len(clienListe) - 1):
                clienListe[i + 1][0].send(s.encode())

        except:
            print("erreur send")
