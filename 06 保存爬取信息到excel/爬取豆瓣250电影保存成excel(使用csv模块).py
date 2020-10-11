import requests, bs4, csv

with open('豆瓣电影二百五.csv','w',newline='',encoding='utf-8') as f:

    writer = csv.writer(f)
    writer.writerow(['排名','电影名','推荐语','链接'])

    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url, headers=headers)
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")

        for titles in bs.find_all('li'):
            num = titles.find('em',class_="").text
            title = titles.find('span', class_="title").text
            comment = titles.find('span',class_="rating_num").text
            url_movie = titles.find('a')['href']

            if titles.find('span',class_="inq") != None:
                tes = titles.find('span',class_="inq").text
                # 每次循环都写入一次
                writer.writerow([num,title,comment,tes,url_movie])
                # print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
            else:
                # 每次循环都写入一次
                writer.writerow([num,title,comment,'',url_movie])
                # print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)


