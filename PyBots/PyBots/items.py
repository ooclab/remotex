# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    url = scrapy.Field()
    
    # http://coding.net =>  coding_net_123  其中 123 是每个 item 的 id 
    uniq_id = scrapy.Field()
   
    # 计算之后的发布日期
    date = scrapy.Field()

    # 3 天之前, 之类的
    date_str = scrapy.Field(serializer=str)
    
    # 价格 
    price = scrapy.Field()
   
    # 阅读数, 报名数之类
    reads = scrapy.Field()
    
    # 项目图片
    cover = scrapy.Field()

    # 语言, 时间限制等 , 数组
    tags = scrapy.Field()

    # 项目的详细说明 
    content = scrapy.Field()

    # 项目发布人或公司简介
    company = scrapy.Field()

