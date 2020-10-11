import requests,gevent
from bs4 import BeautifulSoup
from gevent import monkey
from gevent.queue import Queue
monkey.patch_all()
work = Queue()

url = 'http://www.mtime.com/top/tv/top100/'


url_list = ['http://www.mtime.com/top/tv/top100/']
for i in range(9):
    url = url_list[0]+'index-'+str(i+1)+'.html'
    url_list.append(url)

for url in url_list:
    work.put_nowait(url)

def crawel():
    while not work.empty():
        url = work.get_nowait()
    
res = requests.get(url)
res = res.text
soup = BeautifulSoup(res,'html.parser')
films = soup.find_all(class_='mov_con')
for film in films:
    film_name = film.find('h2').text
    rest_info = film.find_all('p')
    derector = rest_info[0].text
    actor = rest_info[1].text
    try:
        intro = film.find(class_='mt3').text
    except:
        intro = ''
    print(film_name+'\n'+derector+'\n'+actor+'\n'+intro)
    print('-----------')