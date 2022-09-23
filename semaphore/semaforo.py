from threading import Thread, Semaphore

semaforo = Semaphore(1)

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1
# Crear una aplicacion en el cual descargaran 10 recursos doferentes integrando el concepto de semaforo

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire()
        crito(self.id)
        semaforo.release()

threads_semaphore = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for t in threads_semaphore:
    t.start()

