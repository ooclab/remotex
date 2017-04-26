# -*- coding: utf-8 -*-
import scrapy
import json
from PyBots.items import JobItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re


class Tech2ipoSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["pro.lagou.com"]
    start_urls = [
        "https://pro.lagou.com/project/"
    ]

    def parse(self, response):
        pass

    def parse_contents(self, response):
        pass