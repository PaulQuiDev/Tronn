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


def ConnectionClient(queue):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # = = = = = = = = = = = == = = = = =  = = ==  = =
    try :
        sck.connect(("127.0.0.1", 8888))
        print("requete connection")
    except :
        return "E"

    # connecter =  = = = = = = = = = = = = = = = = =

    thread = threading.Thread(group=None, target=receptionClient, args=(sck, queue))
    thread.start()

    return sck


def Send(message, sck):
    sck.send(message.encode())
    #print("client : " + message)


if __name__ == "__main__":
    queu = multiprocessing.Queue()

    sck = ConnectionClient("conecter", queu)

    while True:
        s = input()
        # print(queu.get())
        Send(s, sck)
