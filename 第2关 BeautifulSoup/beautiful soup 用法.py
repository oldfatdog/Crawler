import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='books')

print('hello')
for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    brief = item.find(class_='info')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)
