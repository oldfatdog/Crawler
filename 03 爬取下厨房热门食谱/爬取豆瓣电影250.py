import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
a = 0
film_list = []
while a <226:
    url = 'https://movie.douban.com/top250?start='+str(a)+'&filter='

    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    soup_list = soup.find('ol',class_="grid_view").find_all('li')

    for i in soup_list:
        film_info = []
        film_name = []

        name_title = i.find_all('span',class_="title")
        name_other = i.find('span',class_="other")
        for j in name_title:
            film_name.append(j.text)
        film_name.append(name_other.text)
        film_info.append(film_name)

        film_info.append(i.find('span',class_="rating_num").text)

        try:
            film_info.append(i.find('span',class_="inq").text)
        except:
            film_info.append('无推荐语')

        film_info.append(i.find('a')['href'])

        film_list.append(film_info)
    a = a + 25
    
rank = 0
for i in film_list:
    rank += 1
    name = i[0]
    star = i[1]
    recomend = i[2]
    address = i[3]
    print('排名:%s\n电影名:%s\n评分:%s\n推荐语:%s\n网址:%s'%(rank,name,star,recomend,address))
    print('--------------------------------')