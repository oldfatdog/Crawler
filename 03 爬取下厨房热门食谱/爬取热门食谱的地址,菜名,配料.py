import requests
from bs4 import BeautifulSoup 

res = requests.get('http://www.xiachufang.com/explore/')
soup = BeautifulSoup(res.text,'html.parser')
foodlist = soup.find_all(class_='info pure-u')
foodinfo = []
for item in foodlist:
    name = item.find(class_="name").text.strip()
    food = item.find('a').text.strip()
    foodaddress = 'http://www.xiachufang.com/'+item.find('a')['href']
    elli = item.find(class_='ing ellipsis').text.strip()
    foodinfo.append([name,foodaddress,elli])
print(foodinfo)
