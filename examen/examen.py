import threading
import time 

mutex = threading.Lock()

def comer(idPersona):
    palillo = 2
    print()
    print(f"La persona {idPersona} tiene {palillo} palillos y empezó a comer")
    time.sleep(3)
    print(f"La persona {idPersona} dejo el palillo"'\n'f"La persona {idPersona} dejo de comer")
    time.sleep(3)

class Persona(threading.Thread):
    def __init__(self, idPersona):
        threading.Thread.__init__(self)
        self.idPersona = idPersona

    def run(self):
        mutex.acquire()
        comer(self.idPersona)
        mutex.release()

personas = [Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7), Persona(8)]

for p in personas:
    p.start()