# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class PybotsPipeline(object):
    
    def __init__(self):
        self.headers = {
            'authorization':'Basic dXNlcjE6NDVhYTczNmYxZjY2ZTUxMWEyOWIwYzJi',
            # 'authorization': 'Basic ZGV2LXVzZXIxOmJlNzZhNjQ3ODhlODdhNDMyYzg3ZmYyZjUwN2Q4', #test env
            'Content-Type':'application/json',
            'cache-contro':'no-cache',
        }
        # self.url = 'https://remotex.ooclab.org/api/spider/jobx/job'
        self.url = 'http://114.215.221.229/api/spider/jobx/job'
    
    def process_item(self, item, spider):
        print dict(item)
        res = requests.post(self.url, headers=self.headers, json=dict(item))
        print res
