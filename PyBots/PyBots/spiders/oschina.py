# -*- coding: utf-8 -*-
import datetime
import re

import scrapy
from PyBots.items import JobItem


class OSchinaSpider(scrapy.Spider):
    name = '开源中国'
    domain = ['zb.oschina.net']

    def start_requests(self):
        urls = ['https://zb.oschina.net/?sort=4']
        # urls = ['https://zb.oschina.net']
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
        item['release_date'] = self.utc_rfc3339_string(
            release_date, format='%Y-%m-%d')
        item['expire_date'] = ''

        yield item

    def utc_rfc3339_string(self, str_date, format='%Y-%m-%d %H:%M:%S'):
        '''转化 datetime(UTC) 为 rfc3339 格式字符串'''
        dt = datetime.datetime.strptime(str_date, format)
        return dt.isoformat('T') + 'Z'
