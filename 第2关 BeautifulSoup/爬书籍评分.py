import requests 
from bs4 import BeautifulSoup as BS

res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
soup = BS(res.text,'html.parser')
tag_content = soup.find_all(class_="product_pod")

for item in tag_content:
    star = item.find(class_='star-rating')['class'][1]
    name = item.find('h3').text
    price = item.find(class_='price_color').text
    print(' name:%s\n star:%s\n price:%s'%(name,star,price))
    print('------------------')