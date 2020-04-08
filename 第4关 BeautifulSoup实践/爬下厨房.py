import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签
info = list_foods.find('p')
print(info)
'''
name = info.find('a')
link = name['href']
print(name.text)'''