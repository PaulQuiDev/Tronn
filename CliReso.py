import socket 
import multiprocessing
import threading

#importe ===========================



#initialiser les truc =============================

def receptionClient(sck,queue):
    while True:
         #or 'with lock:' (instead of acquire and release)
        data = sck.recv(1024)
        if len(data) == 0:
            print('déconnecter du serveur ¯\_(ツ)_/¯')
            sck.close()
            break
        queue.put(data)
    
#les fonctions =======================

def ConnectionClient(message, queue):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # = = = = = = = = = = = == = = = = =  = = ==  = =
    sck.connect(('127.0.0.1', 8888))
    print("requete connection")

    #connecter =  = = = = = = = = = = = = = = = = =

    thread = threading.Thread(group = None, target = receptionClient,args=(sck,queue))
    thread.start()

    while True:
        sck.send(message.encode())

