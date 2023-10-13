import threading
lock = threading.Lock()

def func():
    while True:
        with lock:
            print("loopy")

thread = threading.Thread(group=None, target=func)
#on ne met pas de () apres func car on n'appelle pas la fonction, on donne la fonction comme target

thread.start()
while True:
    lock.acquire()
    print("yolo")
    lock.release()
# les deux while essaye d'acceder en meme temps au meme objet (le terminal) 
# cela genere un resultat indefinit
#le lock permet de faire attendre l'autre programme lorsque le variable est en cours d'utilisation

import multiprocessing
queue = multiprocessing.Queue()
queue.put(1)
queue.get()
