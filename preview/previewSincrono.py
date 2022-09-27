import requests
import time

sitios = [ "https://www.google.com/intl/es/drive/","https://www.google.com.mx/","https://web.whatsapp.com/","https://twitter.com/?lang=es","https://www.python.org/",
            "https://www.amazon.com.mx/","https://www.youtube.com/","https://github.com/","https://open.spotify.com/","https://www.inboundcycle.com/blog-de-inbound-marketing/que-son-las-redirecciones-301-y-302-y-como-configurarlas",
            "https://www.netflix.com/mx/","https://www.hbomax.com/mx/es","https://www.canva.com/es_419/","https://cinepolis.com/","https://www.primevideo.com/hp/video/offers/nonprimehomepage/ref=dv_web_force_root?_encoding=UTF8&dvah=nonprimehomepage",
            "https://playvalorant.com/en-us/","https://www.dailymotion.com/mx","https://www.mozilla.org/es-MX/firefox/new/","https://www.microsoft.com","https://web.telegram.org/",
            "https://music.apple.com/","https://www.tumblr.com","https://www.craigslist.org","https://www.howtogeek.com","https://www.hostinger.mx/tutoriales/http-302"
        ]

def url_ok(url):
    r=requests.head(url)
    if r.status_code  == 200:  
        time.sleep(240)
        r = requests.head(url)
        if r.status_code == 200:
            print(f'La página: {url} tiene un estatus actual: '+str(r.status_code)+' La página esta activa')
        else:
            print(f'La página: {url} tiene un estatus actual: '+str(r.status_code)+' La página esta inactiva o no fue encontrada')    
    else:
        print(f'La página: {url} tiene un estatus actual: '+str(r.status_code)+' La página esta inactiva o no fue encontrada')
            
for url in sitios:
    url_ok(url)
    time_end = time.time()