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
ua = UserAgent()
headers = {
    'User-Agent': ua.random
}
URL = "https://music.163.com/artist?id=3684"

URL2 = 'http://music.163.com/song/media/outer/url?id='
res = Request(URL,headers=headers)

with urlopen(res) as html:
    text = html.read().decode('utf-8')

doc = etree.HTML(text)
links = doc.xpath("//ul[@class='f-hide']/li/a/@href")
songs = doc.xpath("//ul[@class='f-hide']/li/a/text()")

ids = [ link[9::] for link in links]


for sid,title in zip(ids,songs):
    time.sleep(1)
    req2 = Request(URL2 + str(sid),headers=headers)
    with urlopen(req2) as html:
        urlretrieve(html.geturl(),"songs/%s.mp3"%title)
        print("songs/%s.mp3 下载完成"%title)
