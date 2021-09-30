import requests
from bs4 import BeautifulSoup
from random import choice
from getuseragent import UserAgent


#
#request modülü versiyon 2.23.0 olmalı
#bu fonksiyon rastgele proxy adreslerini döndürüyor

def GetProxy():
    url = 'https://free-proxy-list.net/'
    #yukarıdaki urlnin alternatifleri var
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return {'https': "https://"+choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), list(map(lambda x: x.text, soup.find_all('td')[1::8])))))))}

def UseProxy(url):
    ua = UserAgent()
    currentUA=ua.Random()
    print(currentUA)
    count=0


    while True:
        headers = {"User-agent": currentUA}
        try:

            proxy = GetProxy()
            print(proxy)
            r = requests.get(url,headers=headers,proxies=proxy,timeout=7)

            if r.status_code == 200:
                print("************")
                print('Çalışan proxy = ',proxy)
                print('çalışan header: ',currentUA)
                break
        except Exception as ex:
            print(ex)
            count+=1
            print(count)
            if count >10:
                currentUA=ua.Random()
                count=0


            print('Yukarıdaki proxy denendi ancak çalışmıyor ^ ')
            pass

    return proxy
url = 'https://www.instagram.com/'
proxy = UseProxy(url)
print("kullanılacak proxy:",proxy)

