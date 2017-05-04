# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import re

import scrapy
from PyBots.items import JobItem


class OSchinaSpider(scrapy.Spider):
    name = 'oschina'
    domain = ['zb.oschina.net']

    def start_requests(self):
        urls = ['https://zb.oschina.net/?sort=4']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath(
            '//div[@class="pof-margin-wrapper"]/article/a/@href'
        ).extract()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = JobItem()

        categories_part_1 = response.xpath(
            '//div[@class="box-aw"]/div[1]/a['
            '@class="bn bn-icon bn-small light-green"]/text()'
        ).extract()
        categories_part_2 = response.xpath(
            '//div[@class="box-aw"]/div[1]/span['
            '@class="text-gray"]/text()'
        ).extract()

        skills = ''
        skills_block = response.xpath(
            '//div[@class="project-attr"]/text()'
        ).extract()
        for skill in skills_block:
            value = skill.replace(u'\xa0', '').encode("UTF8").split(':')
            if value[0].strip() == '技能要求':
                skills = value[1].strip()

        release_date = response.xpath(
            '//span[@class="publish-date text-gray"]/text()'
        ).extract()[1].split(":")[1].strip()

        item['platform'] = u'OSChina'
        item['title'] = response.xpath(
            '//h2[@class="wrap"]/text()'
        ).extract_first().strip()
        item['url'] = response.url
        item['body'] = ''.join(response.xpath(
            '//div[@class="simditor-body wrap"]//text()'
        ).extract()).strip()
        item['checksum'] = '{}_{}'.format(
            'zb_oschina_net', response.url.split('/')[-1]
        )
        item['city'] = ''
        price = response.xpath(
            '//div['
            '@class="box box-fr column justify reward-amount"'
            ']/div[1]/span/text()'
        ).extract_first().strip().replace(',', '')
        if re.search('\d+', price):
            price = int(re.search('\d+', price).group())
        else:
            price = 0
        item['price'] = price
        item['categories'] = categories_part_1 + categories_part_2
        item['roles'] = []
        item['skills'] = [skills]
        item['release_date'] = self.str2date(release_date)
        item['expire_date'] = ''

        yield item

    def str2date(self, date_str):
        if re.search('\d{4}-\d{2}-\d{2}', date_str):
            _d = re.search('\d{4}-\d{2}-\d{2}', date_str).group()
            dt = datetime.strptime(_d, '%Y-%m-%d')
            return dt.isoformat('T') + 'Z'

        if re.search('\d+', date_str):
            num = int(re.search('\d+', date_str).group())
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
