# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PybotsPipeline(object):
    
    def __init__(self):
        pass

    def process_item(self, item, spider):
        print item
        # 此处以后可以添加插入数据库的操作
        return item
