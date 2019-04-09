# 一、爬取图片
from urllib.request import *
from lxml import etree
from fake_useragent import UserAgent
import time

# url = "http://unsplash.lofter.com"
#
# with urlopen(url) as html:
#     text = html.read().decode("utf-8")
#
# doc = etree.HTML(text)
# links = doc.xpath("//div[contains(@class,'m-post-img')]/a/span/img/@src")
#
# # 下载资源
# for i in range(len(links)):
#     time.sleep(1)
#     print("正在下载第%s个"%i)
#     urlretrieve(links[i],'img/%s.jpg'%i)
#     urlcleanup()

# 二、爬取音乐
# ua = UserAgent()
# headers = {
#     'User-Agent': ua.random
# }
# URL = "https://music.163.com/artist?id=3684"
#
# URL2 = 'http://music.163.com/song/media/outer/url?id='
# res = Request(URL,headers=headers)
#
# with urlopen(res) as html:
#     text = html.read().decode('utf-8')
#
# doc = etree.HTML(text)
# links = doc.xpath("//ul[@class='f-hide']/li/a/@href")
# songs = doc.xpath("//ul[@class='f-hide']/li/a/text()")
#
# ids = [ link[9::] for link in links]
#
#
# for sid,title in zip(ids,songs):
#     time.sleep(1)
#     req2 = Request(URL2 + str(sid),headers=headers)
#     with urlopen(req2) as html:
#         urlretrieve(html.geturl(),"songs/%s.mp3"%title)
#         print("songs/%s.mp3 下载完成"%title)

# 单例模式
#
# class Foo(object):
#     __obj = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__obj:
#             cls.__obj = super().__new__(cls)
#             return cls.__obj
#         else:
#             return cls.__obj
#
#     def __init__(self,name):
#         self.name = name
#     def say(self):
#         print(self.name)
#
# a = Foo("horns")
# b = Foo('xm')
# a.say()
# b.say()

# 一、操作表格

# import xlwt,pickle
#
# wb = xlwt.Workbook() # 创建表格对象
# ws = wb.add_sheet("abc") #创建表
#
#
# with open("top250.txt",'rb') as f:
#     arr = pickle.load(f)
#
# index = 0
# for arr2 in arr:
#     for title,url in arr2:
#         # # 序号
#         ws.write(index,0,index+1)
#         # title
#         ws.write(index,1,title)
#         # url
#         ws.write(index,2,url)
#         # print(index,title,url)
#         index+=1
#
# wb.save("豆瓣电影.xls")

# 爬取豆瓣

from urllib.request import *
import requests
import pickle,fake_useragent
from lxml.etree import *

with open('top250.txt','rb') as f:
    arr = pickle.load(f)
lists = []
for arr1 in arr:
    for title,url in arr1:
        lists.append(url)

ua = fake_useragent.UserAgent()
header = {
    'User-Agent':ua.random
}
def spider(url):
    # req = Request(url,headers=header)
    # with urlopen(req) as html:
    #     text = html.read().decode()
    res = requests.get(url,headers=header,proxies={
        'http':'http://39.108.168.155:8118',
        'https': 'https://39.108.168.155:8118',
    })
    doc = HTML(res.text)
    # 导演
    pl1 = "/".join(doc.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a[1]/text()"))
    # 编剧
    pl2 = "".join(doc.xpath("//div[@id='info']/span[2]/span[@class='attrs']/a/text()"))
    # 主演
    pl3 = "/".join(doc.xpath("//div[@id='info']/span[3]/span[@class='attrs']/a/text()"))
    # 类型
    pl4 = "/".join(doc.xpath("//div[@id='info']/span[@property='v:genre']/text()"))
    # 剧情简介
    pl5 = doc.xpath("//span[@property='v:summary']/text()")[0].strip()

    return {
        'dir':pl1,
        'edit':pl2,
        'actor':pl3,
        'type':pl4,
        # 'dis':pl5
    }


data = []
for url in lists:
    # print(url)
    res = spider(url)
    print(res)



