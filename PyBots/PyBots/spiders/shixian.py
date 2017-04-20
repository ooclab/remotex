#coding:utf8
import scrapy
from PyBots.items import JobItem
import re
import time

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
        #大约 19 小时前发布 1 天前发布 大约 1 个月前发布 大约 1 年前发布 
        item['title'] = response.xpath('//article[@class="job-show"]/h1[@class="title"]/text()').extract_first().strip()
        item['url'] = response.url
        item['uniq_id'] = response.url.split('/')[-1]
        item['date_str'] = response.xpath('//small[@class="time"]/text()').extract_first().strip()
        item['date'] = self.str2date(item['date_str'])
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

    def str2date(self, date_str):
        if re.search('\d+',date_str):
            num = int(re.search('\d+',date_str).group())
        if u'分钟' in date_str:
            ts = time.time() - num*60
        elif u'小时' in date_str:
            ts = time.time() - num*60*60
        elif u'天' in date_str:
            ts = time.time() - num*60*60*24
        elif u'月' in date_str:
            ts = time.time() - num*60*60*24*30
        elif u'年' in date_str:
            ts = time.time() - num*60*60*24*30*12
        else:
            ts = time.time()
       
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
