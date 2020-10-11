# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


import scrapy
# 导入scrapy


class JindongItem(scrapy.Item):
    # 定义一个类DoubanItem，它继承自scrapy.Item
    title = scrapy.Field()
    # 定义书名的数据属性
    author = scrapy.Field()
    # 定义作者信息的数据属性
    price = scrapy.Field()
    # 定义价格的数据属性
