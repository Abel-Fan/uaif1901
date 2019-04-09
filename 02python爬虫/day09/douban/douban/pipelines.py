# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

# 筛选
class DoubanPipeline(object):
    def process_item(self, item, spider):
        # 去除 肖申克的救赎 和 霸王别姬
        if item['title'] in ['肖申克的救赎','霸王别姬']:
            raise DropItem("过滤%s"%item['title'])
        else:
            return item

# 保存数据
class DoubanPipeline2:
    def process_item(self,item,spider):
        with open('db.txt','a',encoding="utf8") as f:
            f.write("%s %s %s"%(item['title'],item['info'],item['rating_num']))
            f.write("\n")
        return item



