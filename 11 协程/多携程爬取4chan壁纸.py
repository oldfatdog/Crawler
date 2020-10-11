from gevent import monkey
monkey.patch_all()
import gevent,requests,time
from gevent.queue import Queue
from bs4 import BeautifulSoup # 调用BeautifulSoup库
work = Queue()
start = time.time()

def download_all_img_address(adderss):

    all_img_address = []
    res = requests.get(adderss)    # 返回一个Response对象，赋值给res
    html = res.text    # 把Response对象的内容以字符串的形式返回
    soup = BeautifulSoup( html,'html.parser')    # 把网页解析为BeautifulSoup对象
    items = soup.find_all(class_="fileThumb")

    for item in items:
        img_address = item['href']
        all_img_address.append(img_address)
    print('已下载全部图片地址')
    return all_img_address
  
   
def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get('https:'+url)
        res = res.content
        with open(url[-17:],'wb') as img:
            img.write(res)
        print(str(work.qsize()).ljust(5),end='\r')


def start_download():
    address = input('请输入网址')
    all_address = download_all_img_address(address)

    for url in all_address:
        work.put_nowait(url)

    tasks_list = []
    # 10只爬虫一起爬
    for x in range(10):
        task = gevent.spawn(crawler)
        tasks_list.append(task)

    gevent.joinall(tasks_list)

    end = time.time()
    print(end - start)

start_download()