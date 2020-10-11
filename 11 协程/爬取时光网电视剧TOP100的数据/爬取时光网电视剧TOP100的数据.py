import requests
from bs4 import BeautifulSoup

import gevent
from gevent.queue import Queue

import csv

# 创建excel文件保存爬取结果
with open('时光网top100.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['排名', '剧集名', '导演', '主演', '简介'])

# 获取目标网址
url_list = ['http://www.mtime.com/top/tv/top100/',
            'http://www.mtime.com/top/tv/top100/index-2.html',
            'http://www.mtime.com/top/tv/top100/index-3.html',
            'http://www.mtime.com/top/tv/top100/index-4.html',
            'http://www.mtime.com/top/tv/top100/index-5.html',
            'http://www.mtime.com/top/tv/top100/index-6.html',
            'http://www.mtime.com/top/tv/top100/index-7.html',
            'http://www.mtime.com/top/tv/top100/index-8.html',
            'http://www.mtime.com/top/tv/top100/index-9.html',
            'http://www.mtime.com/top/tv/top100/index-10.html']


# 把网址放到queue列表中
work = Queue()

for url in url_list:
    work.put_nowait(url)

# 创建爬虫方法


def crawler():

    # 当queue列表中有网址时就进行爬取
    while not work.empty():

        # 从queue列表中拿取网址
        url = work.get_nowait()

        # 获取网页信息并用beautifulsoup处理
        res = requests.get(url)
        res = res.text
        soup = BeautifulSoup(res, 'html.parser')

        # 在soup中找到电视剧信息，输出列表
        films = soup.find_all(class_='mov_con')
        for film in films:
            film_name = film.find('h2').text
            rest_info = film.find_all('p')
            director = rest_info[0].text

            # 获取主演信息，如果没有就输出空值
            try:
                actor = rest_info[1].text
            except:
                actor = ''

            # 获取简介信息，如果没有就输出空值
            try:
                intro = film.find(class_='mt3').text
            except:
                intro = ''

            # 结果写入excel表中
            with open('时光网top100.csv', 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([film_name, director, actor, intro])


# 创建任务列表
task_list = []

# 创建任务
for t in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)

# 执行task_list中的所有任务
gevent.joinall(task_list)
