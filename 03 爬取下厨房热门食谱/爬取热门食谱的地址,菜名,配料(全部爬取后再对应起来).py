# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_films = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_films = BeautifulSoup(res_films.text,'html.parser')

# 查找包含菜名和URL的<p>标签
tag_name = bs_films.find_all('span',class_='title')
tag_other_name = bs_films.find_all('span',class_='other')

tag_star = bs_films.find_all('span',class_='rating_num')

tag_recomed = bs_films.find_all('span',class_='inq')
# 查找包含食材的<p>标签
tag_url = bs_films.find_all('div',class_='hd')
url = []
for i in tag_url:
    film_url = tag_url.find('a')
    url.append(film_url['href'])

# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    full_name = tag_name[x].text+tag_other_name[x].text
    list_film =[x,full_name,tag_star[x].text,tag_recomed[x].text,url[x]]     # 将信息添加进list_all    
    list_all.append(list_film)
# 打印
print(list_all)