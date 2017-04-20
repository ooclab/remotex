# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    uniq_id = scrapy.Field()
    date = scrapy.Field()# 实现网没有
    date_str = scrapy.Field(serializer=str)
    price = scrapy.Field()
    reads = scrapy.Field()
    cover = scrapy.Field()# 实现网没有
    tags = scrapy.Field()# list
    content = scrapy.Field()
    company = scrapy.Field()