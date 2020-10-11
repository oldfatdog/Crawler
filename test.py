import bs4
import requests
from bs4 import BeautifulSoup

url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-1'

res = requests.get(url)
res = BeautifulSoup(res.text, 'html.parser')
datas = res.find('ul', class_="bang_list clearfix bang_list_mode")
datas = datas.find_all('li')

for data in datas:
    name = data.find('div', class_='name').text
    author = data.find('div', class_='publisher_info').text
    price = data.find('span', class_='price_n').text
