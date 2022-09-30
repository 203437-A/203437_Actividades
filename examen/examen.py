import threading
import time 

mutex = threading.Lock()

def comer(idPersona):
    palillo = 2
    print()
    print(f"La persona {idPersona} tiene {palillo} palillos y empezó a comer")
    time.sleep(1)
    print(f"La persona {idPersona} dejo el palillo"'\n'f"La persona {idPersona} dejo de comer")
    time.sleep(1)

class Persona(threading.Thread):
    def __init__(self, persona):
        threading.Thread.__init__(self)
        self.persona = persona

    def run(self):
        mutex.acquire()
        comer(self.persona)
        mutex.release()

personas = [Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7), Persona(8)]

for p in personas:
    p.start()