# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import re

import scrapy
from PyBots.items import JobItem


class ShixianSpider(scrapy.Spider):
    name = "shixian"
    domain = 'https://www.shixian.com'
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh,en-US;q=0.8,en;q=0.6,zh-CN;q=0.4,zh-TW;q=0.2',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'shixian.com',
            'Upgrade-Insecure-Requests':'1',
    }

    def start_requests(self):
        urls = ['https://shixian.com/jobs']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = self.parse_index(response)
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_detail,
                headers=self.headers
            )

    def parse_index(self, response):
        urls = []
        job_list = response.xpath('//div[@class="job-list"]/div/div/a')
        for job in job_list:
            url =  'https://shixian.com%s'%job.xpath('./@href').extract_first()
            urls.append(url)
        return urls

    def parse_detail(self, response):
        item = JobItem()
        #大约 19 小时前发布 1 天前发布 大约 1 个月前发布 大约 1 年前发布
        item['platform'] = u'实现网'
        item['title'] = response.xpath('//article[@class="job-show"]/h1[@class="title"]/text()').extract_first().strip()
        # print('title ==>', title)
        item['url'] = response.url
        item['body'] = ''.join(response.xpath('//div[@class="content"]/p//text()').extract()).strip()
        item['checksum'] = '{}_{}'.format( 'shixian_com', response.url.split('/')[-1] )
        item['city'] = response.xpath('//ol[@class="breadcrumb jobs md-no-padding"]/li/a/text()').extract_first().strip()
        item['price'] = int(response.xpath('//strong[@class="price"]/text()').re('\d+')[0])
        release_date = response.xpath('//small[@class="time"]/text()').extract_first().strip()
        item['release_date'] = self.str2date(release_date)
        expire_date = response.xpath('//section[@class="info clearfix"]/dl/dd/span/text()')[3].extract().strip()
        item['expire_date'] = self.str2date(expire_date)
        #item['view_count'] = int(response.xpath('//div[@class="pull-right text-muted"]/text()').re('\d+')[0])
        item['categories'] = response.xpath('//section[@class="info clearfix"]/dl/dd/span/text()')[0].extract().strip().split('/')
        item['roles'] = [response.xpath('//ol[@class="breadcrumb jobs md-no-padding"]/li/a/text()')[1].extract().strip()]
        item['skills'] = response.xpath('//section[@class="skill-tags clearfix"]/dl/dd/text()').extract()
        yield item

    def str2date(self, date_str):
        if re.search('\d{4}-\d{2}-\d{2}',date_str):
            _d = re.search('\d{4}-\d{2}-\d{2}',date_str).group()
            dt = datetime.strptime(_d, '%Y-%m-%d')
            return dt.isoformat('T') + 'Z'

        if re.search('\d+',date_str):
            num = int(re.search('\d+',date_str).group())
        now = datetime.now()
        if u'分钟' in date_str:
            dt = now - timedelta(minutes=num)
        elif u'小时' in date_str:
            dt = now - timedelta(hours=num)
        elif u'天' in date_str:
            dt = now - timedelta(days=num)
        elif u'月' in date_str:
            dt = now - timedelta(days=num*30)
        elif u'年' in date_str:
            dt = now - timedelta(days=num*365)
        else:
            dt = now

        return dt.isoformat('T') + 'Z'
