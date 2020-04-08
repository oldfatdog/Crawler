import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
soup = BeautifulSoup(res.text,'html.parser')
target_list = soup.find_all('article')

for item in target_list:
    time = item.find(class_='entry-date').text
    title = item.find(class_='entry-title').text
    summary = item.find(class_='entry-summary').text
    print('发布日期:%s\n文章标题:%s\n文章简介:%s'%(time,title,summary),end='')
    print('-----------------------------')
