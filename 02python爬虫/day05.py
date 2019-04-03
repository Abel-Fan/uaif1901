#爬虫定义
"""
网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
"""
#爬虫分类
# 通用爬虫、聚焦爬虫
# 工作流程
# 1、设置爬取地址，设置请求头
# 2、解析页面，获取所需信息
# 3、数据存储

# robots协议
"""
Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。
"""

# 常用工具

# builtwith
# whois

# import whois,builtwith
#
# domain = whois.query("http://wordpress.com")
# # print(domain.__dict__)
# # builtwith('http://wordpress.com')


# 解析内容
# 1、XPath
# 通过路径格式获取文档节点
# 安装  pip install lxml
#

from lxml import etree


str1 = """
<div class="box">
    <ul>
        <li class='item0'>
            <a class='link0' href='https://www.baidu.com/'>百度</a>
        </li>
        
        <li class='item1'>
            <div></div>
            <a class='link1 link3' href='https://www.sxuek.com/'>优逸客1</a>
        </li>
        
        <li class='item2'>
            <a class='link2'>优逸客2</a>
            <div></div>
            <div></div>
        </li>
    </ul>
</div>
<div></div>
"""
#
# html = etree.HTML(str1)
# links = html.xpath("//div/ul/li/a[contains(@class,'link1')]")  # xpath 遵循xpath规则
# print(links)

#http协议

# urllib模块

# 组件
# request  打开和阅读URL地址的包
# error 包含 urllib.request 抛出的异常
# parse 用于处理 URL
# urllib.robotparser 用于解析 robots.txt 文件

# 一 request
# from urllib import request
from urllib.request import *
from lxml import etree
import pickle
import time
# arr = []
#
# url = "https://movie.douban.com/top250?start="
# urls = [ url+str(i) for i in range(0,250,25)]
#
# def spider(link):
#     time.sleep(1)
#     print("正在爬取:%s"%link)
#     with urlopen(link) as html:
#         text = html.read().decode("utf-8")
#     doc = etree.HTML(text)
#     titles = doc.xpath("//ol[@class='grid_view']/li/div/div[@class='info']/div[@class='hd']/a/span[1]/text()")
#     links = doc.xpath("//ol[@class='grid_view']/li/div/div[@class='info']/div[@class='hd']/a/@href")
#     arr.append(list(zip(titles,links)))
#
#
# for link in urls:
#     spider(link)
#
#
# with open("./top250.txt",'wb') as f:
#     pickle.dump(arr,f)



with open("./top250.txt",'rb') as f:
    obj = pickle.load(f)


for item in obj:
    print(item)




# with urlopen(url) as html:
#     text = html.read().decode('utf8')
#
# with open("./../../250.html",'r',encoding="utf-8") as f:
#     text = f.read()

# doc = etree.HTML(text)
# titles = doc.xpath("//ol[@class='grid_view']/li/div/div[@class='info']/div[@class='hd']/a/span[1]/text()")
# links = doc.xpath("//ol[@class='grid_view']/li/div/div[@class='info']/div[@class='hd']/a/@href")
#
# print(list(zip(titles,links)))