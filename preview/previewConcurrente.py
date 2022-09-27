import requests
import time
from threading import Thread

sitios = [ "https://www.google.com/intl/es/drive/","https://www.google.com.mx/","https://web.whatsapp.com/","https://twitter.com/?lang=es","https://www.python.org/",
            "https://www.amazon.com.mx/","https://www.youtube.com/","https://github.com/","https://open.spotify.com/","https://www.inboundcycle.com/blog-de-inbound-marketing/que-son-las-redirecciones-301-y-302-y-como-configurarlas",
            "https://www.netflix.com/mx/","https://www.hbomax.com/mx/es","https://www.canva.com/es_419/","https://cinepolis.com/","https://www.primevideo.com/hp/video/offers/nonprimehomepage/ref=dv_web_force_root?_encoding=UTF8&dvah=nonprimehomepage",
            "https://playvalorant.com/en-us/","https://www.dailymotion.com/mx","https://www.mozilla.org/es-MX/firefox/new/","https://www.microsoft.com","https://web.telegram.org/",
            "https://music.apple.com/","https://www.tumblr.com","https://www.craigslist.org","https://www.howtogeek.com","https://www.hostinger.mx/tutoriales/http-302"
        ]

def url_ok(url):
    response=requests.head(url)
    if response.status_code  == 200:  
        time.sleep(240)
        response = requests.head(url)
        if response.status_code == 200:
            print(f'La página: {url} tiene un estatus actual: '+str(response.status_code)+' La página esta activa')
        else:
            print(f'La página: {url} tiene un estatus actual: '+str(response.status_code)+' La página esta inactiva o no fue encontrada')    
    else:
        print(f'La página: {url} tiene un estatus actual: '+str(response.status_code)+' La página esta inactiva o no fue encontrada')
            
class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        url_ok(self.url)

h1 = [Hilo(sitios[0]), Hilo(sitios[1]),Hilo(sitios[2]), Hilo(sitios[3]),Hilo(sitios[4]), Hilo(sitios[5]), Hilo(sitios[6]),Hilo(sitios[7]), Hilo(sitios[8]),Hilo(sitios[9]), Hilo(sitios[10]),
      Hilo(sitios[11]),Hilo(sitios[12]),Hilo(sitios[13]), Hilo(sitios[14]),Hilo(sitios[15]), Hilo(sitios[16]), Hilo(sitios[17]),Hilo(sitios[18]), Hilo(sitios[19]),Hilo(sitios[20]), Hilo(sitios[21]),
      Hilo(sitios[22]),Hilo(sitios[23]),Hilo(sitios[24])
]

for h in h1:
    h.start()
