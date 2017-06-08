# -*- coding: utf-8 -*-
import scrapy
import re
from PyBots.items import JobItem

class V2exSpider(scrapy.Spider):
    name = "v2ex"
    allowed_domains = ["https://www.v2ex.com/"]
    start_urls = ['https://www.v2ex.com/?tab=jobs']
    uniq_prefix = 'v2ex_com'

    def parse(self, response):
        for post in response.css( 'div[class="cell item"]'):
            node = (post.css( 'a[class="node"]::text').extract())[0]
            
            if node == u'酷工作' or node == u'外包':
                title = ( post.css( 'span[class="item_title"] a::text').extract() )[0]
                url = (post.css( 'span[class="item_title"] a::attr(href)').extract())[0]
           
                re_id  = re.compile( '/(\d+)#reply' ) 
                _id  = re_id.findall( url )[0]
                uniq_id = '{}_{}'.format( self.uniq_prefix, _id )
                
                self.parse_detail( url )


    def parse_detail( self, url ):
        self.log( item )





