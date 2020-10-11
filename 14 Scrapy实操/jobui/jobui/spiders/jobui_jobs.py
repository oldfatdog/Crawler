import scrapy
import bs4
from ..items import JobuiItem


class JobuiSpider(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = bs.find_all('ul', class_='textlist flsty cfix')
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['herf']
                url = 'http://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
