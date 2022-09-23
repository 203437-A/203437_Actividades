
import time
import concurrent.futures
import threading
import pytube

save = "D:/Downloads/"
link=["https://www.youtube.com/watch?v=DqgK4llE1cw", "https://www.youtube.com/watch?v=wAMZ6KpMGQI", "https://www.youtube.com/watch?v=F5tSoaJ93ac", "https://www.youtube.com/watch?v=r7Rn4ryE_w8", "https://www.youtube.com/watch?v=p00v9ZFhWJM"]
threading_local = threading.local()

def service():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, link)

def get_service():

    # try:
        video0 = pytube.YouTube(link[0])
        video0.streams.first().download(save)

        video1 = pytube.YouTube(link[1])
        video1.streams.first().download(save)
    
        video2 = pytube.YouTube(link[2])
        video2.streams.first().download(save)

        video3 = pytube.YouTube(link[3])
        video3.streams.first().download(save)

        video4 = pytube.YouTube(link[4])
        video4.streams.first().download(save)
    # except:
    #     print("Error")

if __name__ =="__main__":
    init_time= time.time()
    # get_service()
    url_site = ["link"]
    service(url_site)
    end_time=time.time() - init_time
    print(end_time)