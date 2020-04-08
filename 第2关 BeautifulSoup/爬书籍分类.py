import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
nav = soup.find(class_='nav nav-list')
f_leis = nav.find_all('a')
for f_lei in f_leis:
    print(f_lei.text)