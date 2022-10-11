#Funciones producto y consumidor clase bodegaa y 

import random
import queue
import threading
import time

ESPACIO = queue.Queue(10)

class Bodega(threading.Thread):

    def productor():
        while True:
            if ESPACIO.qsize() < 10:
                valor = random.randint(1, 10)
                ESPACIO.put(valor)
                print(f'El productor inserto el producto: {valor}')
                print(f'El espacio actual es: {list(ESPACIO.queue)}')
                time.sleep(5)
            else:
                time.sleep(5)


    def consumidor():
        while True:
            if ESPACIO.qsize() > 0:
                valor = ESPACIO.get()
                print(f'El consumidor agarro el producto: {valor}')
                print(f'El espacio actual es: {list(ESPACIO.queue)}')
                time.sleep(5)
            else:
                time.sleep(5)

    productor = threading.Thread(target=productor)
    consumidor = threading.Thread(target=consumidor)

    productor.start()
    consumidor.start()
