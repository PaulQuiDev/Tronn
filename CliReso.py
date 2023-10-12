import socket
import multiprocessing
import threading


# importe ===========================


# initialiser les truc =============================


def receptionClient(sck, queue):
    while True:
        # or 'with lock:' (instead of acquire and release)
        data = sck.recv(1024)
        if len(data) == 0:
            print("déconnecter du serveur ¯\_(ツ)_/¯")
            sck.close()
            break
        queue.put(data)
        #print(data)


# les fonctions =======================


def ConnectionClient(message, queue):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # = = = = = = = = = = = == = = = = =  = = ==  = =
    print("requete connection")
    try :
        sck.connect(("127.0.0.1", 8888))
        print("conection réusite")
    except :
        print("conection error")
        return "E"
    
        
    # connecter =  = = = = = = = = = = = = = = = = =

    thread = threading.Thread(group=None, target=receptionClient, args=(sck, queue))
    thread.start()

    sck.send(message.encode())
    return sck


def Send(message, sck):
    sck.send(message.encode())


if __name__ == "__main__":
    queu = multiprocessing.Queue()

    sck = ConnectionClient("conecter", queu)

    while True:
        s = input()
        # print(queu.get())
        Send(s, sck)
