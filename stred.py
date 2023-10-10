import multiprocessing

quu = multiprocessing.Queue()
quu.put(1)
quu.put(2)

print(quu.get())
print(quu.get())

print("coucou")
