import socket 
import multiprocessing
import threading

#importe ===========================


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lock = threading.Lock() #?

#initialiser les truc =============================
def func():
    while True:
         #or 'with lock:' (instead of acquire and release)
        data = sck.recv(1024)
        if len(data) == 0:
            print('déconecter du serveur ¯\_(ツ)_/¯')
            sck.close()
            break
        print(data)
    
#les fonctions =======================

# = = = = = = = = = = = == = = = = =  = = ==  = =
sck.connect(('127.0.0.1', 8888))
print("recquet conection")
#coneter =  = = = = = = = = = = = = = = = = =

thread = threading.Thread(group = None, target = func)
thread.start()

while True:
    s = input()
    sck.send(s.encode())

