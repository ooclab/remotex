# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 来源平台
    platform = scrapy.Field() 

    title = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()

    # http://coding.net =>  coding_net_123  其中 123 是每个 item 的 id 
    checksum = scrapy.Field()

    city = scrapy.Field() 

    # 价格 
    price = scrapy.Field()

    # 状态，暂时无用
    status = scrapy.Field()

    # 发布时间
    release_date = scrapy.Field(serializer=str)

    # 过期时间
    expire_date = scrapy.Field(serializer=str)

    # 创建时间
    created = scrapy.Field(serializer=str)

    # 更新时间
    updated = scrapy.Field(serializer=str)

    # 查看数
    view_count = scrapy.Field()

    # 支持数
    vote_up = scrapy.Field()

    # 反对数
    vote_down = scrapy.Field()

    # 兼职类型 list
    categories =scrapy.Field()

    # 兼职岗位 list
    roles = scrapy.Field()

    # 兼职技术 list
    skills = scrapy.Field()

