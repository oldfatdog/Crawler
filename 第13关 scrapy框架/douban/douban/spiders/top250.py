import scrapy
import bs4


class JindongSpider(scrapy.Spider):
    name = 'Jindong'
    allowed_domain = ['bang.dangdang.com']
    start_urls = []

    for x in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + \
            str(x + 1)
        start_urls.append(url)

    def parse(self, response):
        res = bs4.BeautifulSoup(res.text, 'html.parser')
        datas = res.find('ul', class_="bang_list clearfix bang_list_mode")
        datas = datas.find_all('li')

        for data in datas:
            item = JindongItem()

            item[name] = data.find('div', class_='name').text
            item[author] = data.find('div', class_='publisher_info').text
            item[price] = data.find('span', class_='price_n').text

            print(item[name])

            yield item
