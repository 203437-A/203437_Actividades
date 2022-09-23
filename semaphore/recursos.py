from threading import Thread, Semaphore
import pytube

semaforo = Semaphore(1)


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


def crito(id, video):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

    yt = pytube.YouTube(str(video))
    yt.streams.first().download("D:/Downloads")
    print(f'{video} se descargo')
#Crear una aplicacion en el cual descargaran 10 recursos doferentes integrando el concepto de semaforo
class Hilo(Thread):
    def __init__(self, id, video):
        Thread.__init__(self)
        self.id=id
        self.video=video

    def run(self):
        semaforo.acquire()
        crito(self.id, self.video)
        semaforo.release()

threads_semaphore = [Hilo(1, videos[0]), Hilo(2, videos[1]), Hilo(3, videos[2]), Hilo(4, videos[3]), Hilo(5, videos[4]), Hilo(6, videos[5]), Hilo(7, videos[6]), Hilo(8, videos[7]), Hilo(9, videos[8]), Hilo(10, videos[9])]
x=0;
for t in threads_semaphore:
    t.start()
