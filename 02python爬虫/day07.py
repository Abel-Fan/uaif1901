# request
# 动态页面加载 Selenium
# request
# 响应类型为 json
# import json

# json.loads(str)  # 将str转化为dict
# json.dumps(dict)  # 将dict转化为 str

#
# url = "https://www.toutiao.com/stream/widget/local_weather/city/"
# url2 = "https://www.toutiao.com/stream/widget/local_weather/data/?city="
# with urlopen(url2+quote('太原')) as html:
#     text = html.read().decode()
#
#     obj = json.loads(text)
#     print(obj)

import requests
from fake_useragent import UserAgent
from lxml.etree import HTML
import time,pickle
#
# res = requests.get(url)
# print(res.text)
# print(res.content)
# print(res.url)
# print(res.encoding)
# print(res.status_code)

url = "https://www.kuaidaili.com/free/inha/%s/"
ua = UserAgent()
headers={
    "User-Agent":ua.random
}
def getIP(url):
    res = requests.get(url,headers=headers)
    doc = HTML(res.text)
    ips = doc.xpath("//td[@data-title='IP']/text()")
    ports = doc.xpath("//td[@data-title='PORT']/text()")
    arr = [ ip+":"+port for ip,port in zip(ips,ports)]
    return arr
IPS = []
for i in range(1,100):
    time.sleep(1)
    arr = getIP(url%i)
    print(arr)
    IPS+=arr

with open("IPS.txt",'wb') as f:
    pickle.dump(IPS,f)
