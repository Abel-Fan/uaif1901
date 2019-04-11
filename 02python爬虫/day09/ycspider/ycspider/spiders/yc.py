# -*- coding: utf-8 -*-
import scrapy


class YcSpider(scrapy.Spider):
    name = 'yc'
    allowed_domains = ['www.aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%BF%90%E5%9F%8E']

    def parse(self, response):
        hrefs = response.xpath("//td/a/@href").extract()
        print(hrefs)