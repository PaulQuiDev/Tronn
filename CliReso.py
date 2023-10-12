import socket
import multiprocessing
import threading

IP = "192.168.116.212" # PUT SERVER IP HERE

#functions =============================

# listen data send from the sever
def receptionClient(sck, queue):
    while True:
        data = sck.recv(1024)
        if len(data) == 0:
            print("déconnecter du serveur ¯\_(ツ)_/¯")
            sck.close()
            break
        queue.put(str(data.decode("utf-8", errors="ignore")))


# initialize connexion of a client
# the parameter queue permit the storage of recieved informations
def ConnectionClient(queue):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sck.connect((IP, 1234))
        print("requete connection")
    except :
        return "E"

    thread = threading.Thread(group=None, target=receptionClient, args=(sck, queue))
    thread.start()

    return sck

def scanPlayer(sck):
    sck.send("scan".encode())

# send e masage to the server
def Send(message, sck):
    sck.send(message.encode())


# optional main =============================

if __name__ == "__main__":
    queu = multiprocessing.Queue()

    sck = ConnectionClient("conecter", queu)

    while True:
        s = input()
        Send(s, sck)
