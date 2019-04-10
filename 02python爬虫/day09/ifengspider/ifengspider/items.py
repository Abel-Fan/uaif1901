# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IfengspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文章附属信息
    category = scrapy.Field() # 分类
    link = scrapy.Field() # 分类链接
    
    # 文章信息
    title = scrapy.Field() # 标题
    conlink = scrapy.Field() # 文章链接
    date = scrapy.Field() # 日期
    author = scrapy.Field() # 作者
    con = scrapy.Field() # 文章内容
    
