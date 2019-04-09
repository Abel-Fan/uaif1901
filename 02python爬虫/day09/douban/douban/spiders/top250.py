# -*- coding: utf-8 -*-
import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        print(response.text)
