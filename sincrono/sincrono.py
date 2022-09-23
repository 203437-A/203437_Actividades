import requests
import time
import psycopg2

conexion = psycopg2.connect(user='postgres', password='Angel01', host='localhost', port='5432', database='api')
cursor = conexion.cursor()

def get_service ():
    url= "https://randomuser.me/api/?results=2000"
    response= requests.get(url) 
    names= response.json().get('results')
    for name in names:
         write_db(name['name']['first']) 
    print('Los datos se añadieron correctamente')

def write_db (x):
    cursor.execute("insert into names(name) values('"+x+"')")
    conexion.commit()

if __name__ =="__main__":
    init_time= time.time()
    get_service()
    end_time=time.time() - init_time
    print(end_time)
    conexion.close()