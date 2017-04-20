# -*- coding: utf-8 -*-
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
        cities = ['beijing','shanghai','shenzhen','hangzhou','guangzhou','chengdu','nanjing','xian','hubei','xiamen','shandong','suzhou','zhengzhou','fuzhou','changsha','chongqing','tianjin','ningbo','remote','qita']
        jobs = ['ios','android','ui','frontend','backend','pm','operator','tester','full_stack','others']
        # cities = ['beijing']
        # jobs = ['ios']
        for city in cities:
            for job in jobs:
                url = 'https://shixian.com/job/%s?filter=last&territory=%s'%(city,job)
                yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        if 'jobs'in response.url:
            self.parse_detail(response)
            item = self.parse_detail(response)
            yield item
        else:
            urls = self.parse_index(response)
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse_index(self, response):
        urls = []
        # next page 后期可以去掉，每天只抓第一页
        next_url = response.xpath('//ul[@class="pagination"]/li/a[@rel="next"]/@href')
        if len(next_url) > 0:
            url = 'https://shixian.com%s'%next_url.extract_first()
            urls.append(url)
        # jons
        job_list = response.xpath('//div[@class="job-list"]/div/div/a')
        for job in job_list:
            url =  'https://shixian.com%s'%job.xpath('./@href').extract_first()
            urls.append(url)
        return urls

    def parse_detail(self, response):
        item = JobItem()
        item['title'] = response.xpath('//article[@class="job-show"]/h1[@class="title"]/text()').extract_first().strip()
        item['url'] = response.url
        item['uniq_id'] = '{}_{}'.format( 'shixian_com', response.url.split('/')[-1] )
        item['date_str'] = response.xpath('//small[@class="time"]/text()').extract_first().strip()
        item['price'] = int(response.xpath('//strong[@class="price"]/text()').re('\d+')[0])
        item['reads'] = int(response.xpath('//div[@class="pull-right text-muted"]/text()').re('\d+')[0])
        item['content'] = ''.join(response.xpath('//div[@class="content"]/p/text()').extract()).strip()
        item['company'] = ''.join(response.xpath('//section[@class="company"]//text()').extract()).strip()
        tags = []
        for n in response.xpath('//section[@class="info clearfix"]/dl/dd'):
            tag = ''.join(n.xpath('./text()').extract()).strip() + ''.join(n.xpath('./span/text()').extract()).strip()
            tags.append(tag)
        item['tags'] = tags
        return item
