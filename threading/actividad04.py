import time
import requests 
import psycopg2
import pytube
import threading
import concurrent.futures

videos = [ "https://www.youtube.com/watch?v=RSaWHbCSmRI", 
           "https://www.youtube.com/watch?v=Iz0m4R-UV0s", 
           "https://www.youtube.com/watch?v=F5tSoaJ93ac", 
           "https://www.youtube.com/watch?v=r7Rn4ryE_w8", 
           "https://www.youtube.com/watch?v=p00v9ZFhWJM"]

def conectionDB():
    conexion = psycopg2.connect(user='postgres', password='Angel01', host='localhost', port='5432', database='api')
    return conexion

#Descargar 5 videos, escribir en base de datos, por lo menos 2000 registros, 
#la tercera generar una solicitud a raamdomuser de por lo menos 50 usuarios diferentes

def get_services():  
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)

def get_services_BD():
    url= "https://randomuser.me/api/?results=2000"
    response= requests.get(url) 
    print("url utilizada: "+url)
    names= response.json().get('results')
    for name in names:
        data= name['name']['first']
        write_db(data) 
    print("Se han registrado los datos en la BD")

def write_db (x):
    conecBD = conectionDB()
    conexion2=conecBD.cursor()
    conexion2.execute("insert into names(name) values('"+x+"')")
    conecBD.commit()
    conecBD.close()
 
def get_services_videos(videos):
    yt = pytube.YouTube(str(videos))
    yt.streams.first().download("D:/Downloads")
    print(f'{videos} se descargo')

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_services_videos, videos)

if __name__ == '__main__':
    init_time = time.time()
    for x in range(0,50):
       th1=threading.Thread(target=get_services)
       th1.start()
       th1.join()
    th2=threading.Thread(target=get_services_BD)
    th2.start()
    th3=threading.Thread(target=get_services_videos, args=[videos])
    th3.start()
    end_time=time.time() - init_time 
    print(end_time)