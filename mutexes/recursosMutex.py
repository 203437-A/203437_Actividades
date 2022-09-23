import pytube
import threading

# semaforo = Semaphore(1)
mutex= threading.Lock()


videos = [ "https://www.youtube.com/watch?v=RSaWHbCSmRI", 
           "https://www.youtube.com/watch?v=Iz0m4R-UV0s", 
           "https://www.youtube.com/watch?v=F5tSoaJ93ac", 
           "https://www.youtube.com/watch?v=r7Rn4ryE_w8", 
           "https://www.youtube.com/watch?v=p00v9ZFhWJM",  
           "https://www.youtube.com/watch?v=VRQDOFaFqWk",
           "https://www.youtube.com/watch?v=wpsjqOBkD6w",
           "https://www.youtube.com/watch?v=s0JJxPyhOH0",
           "https://www.youtube.com/watch?v=Txn5-dKLFHg",
           "https://youtu.be/1-W6whvn8Bs"
           ]


def crito(video):
    yt = pytube.YouTube(str(video))
    yt.streams.first().download("D:/Downloads")
    print(f'{video} se descargo')
#Crear una aplicacion en el cual descargaran 10 recursos doferentes integrando el concepto de semaforo
class Hilo(threading.Thread):
    def __init__(self, video):
        threading.Thread.__init__(self)
        self.video=video

    def run(self):
        mutex.acquire()
        crito(self.video)
        mutex.release()

hilos = [Hilo(videos[0]), Hilo(videos[1]), Hilo(videos[2]), Hilo(videos[3]), Hilo(videos[4]), Hilo(videos[5]), Hilo(videos[6]), Hilo(videos[7]), Hilo(videos[8]), Hilo(videos[9])]

for h in hilos:
    h.start()
