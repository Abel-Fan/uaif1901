# -*- coding: utf-8 -*-
import scrapy
from ribaospider.items import RibaospiderItem

class RibaoSpider(scrapy.Spider):
    name = 'ribao'
    allowed_domains = ['118.190.150.35:9000']
    start_urls = ['http://118.190.150.35:9000/login']

    def parse(self, response):
        print(response.ydh)
        item = RibaospiderItem()
        item['name'] = 'ydh'
        yield item
        