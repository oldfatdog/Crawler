import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库

address = input('请输入网址')

all_img_address = []
res = requests.get(address)# 返回一个Response对象，赋值给res
html = res.text# 把Response对象的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') # 把网页解析为BeautifulSoup对象
items = soup.find_all(class_="fileThumb")

for item in items:
    img_address = item['href']
    all_img_address.append(img_address)
for i in all_img_address:
    with open('imgaddress.txt','a') as f:
        f.write('https:'+i+'\n')

