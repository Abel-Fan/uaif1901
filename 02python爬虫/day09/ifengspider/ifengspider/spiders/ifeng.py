# -*- coding: utf-8 -*-
import scrapy
from ifengspider.items import IfengspiderItem

class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/ipad']

    def parse(self, response):
        categorys = response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
        links = response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
        for category,link in zip(categorys,links):
            # 记录  标题 以及 标题链接
            # category link
            data = {'category':category,'link':link}
            # 请求分类页面
            yield scrapy.Request(link,meta={'data':data},callback=self.getNewList)
    def getNewList(self,response):
        data = response.meta['data']
        category = data["category"]
        link = data['link']
        titles=[]
        conlinks=[]
        if category == "国际":
            titles += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            conlinks += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        if category=="即时":
            titles += response.xpath("//div[@class='newsList']/ul/li/a/text()").extract()        
            conlinks += response.xpath("//div[@class='newsList']/ul/li/a/@href").extract()
        
        
        
        
        if titles and conlinks:
            for title,conlink in zip(titles,conlinks):
                item = IfengspiderItem()
                item['category'] =  category
                item['link'] =  link
                item['title'] =  title
                item['conlink'] =  conlink
                yield scrapy.Request(conlink,meta={'item':item},callback=self.getNewCon)
        
    def getNewCon(self,response):
        item = response.meta['item']
        if item['category']=="国际":
            con = response.xpath("//div[@id='artical_real']//text()").extract()


        item['con'] = con

        yield item