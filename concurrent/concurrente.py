import requests
import time
import concurrent.futures
import threading
import psycopg2

threading_local = threading.local()

conexion = psycopg2.connect(user='postgres', 
                            password='Angel01', 
                            host='localhost', 
                            port='5432', 
                            database='api')
cursor = conexion.cursor()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service (url):
    url= "https://randomuser.me/api/?results=2000"
    response= requests.get(url) 
    # connection_db()
    print(url)
    names= response.json().get('results')
    for name in names:
        write_db(name['name']['first']) 

def write_db (x):
    cursor.execute("insert into names(name) values('"+x+"')")
    conexion.commit()

if __name__ =="__main__":
    init_time= time.time()
    url_site = ["url"]
    service(url_site)
    end_time=time.time() - init_time
    print(end_time)
    conexion.close


    #Crear una aplicacion para descargar videos de 5 url diferentes 