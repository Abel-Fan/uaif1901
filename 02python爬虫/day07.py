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

# import requests
# from fake_useragent import UserAgent
# from lxml.etree import HTML
# import time,pickle
#
# res = requests.get(url)
# print(res.text)
# print(res.content)
# print(res.url)
# print(res.encoding)
# print(res.status_code)
#
# url = "https://www.kuaidaili.com/free/inha/%s/"
# ua = UserAgent()
# headers={
#     "User-Agent":ua.random
# }
# def getIP(url):
#     res = requests.get(url,headers=headers)
#     doc = HTML(res.text)
#     ips = doc.xpath("//td[@data-title='IP']/text()")
#     ports = doc.xpath("//td[@data-title='PORT']/text()")
#     arr = [ ip+":"+port for ip,port in zip(ips,ports)]
#     return arr
# IPS = []
# for i in range(1,100):
#     time.sleep(1)
#     arr = getIP(url%i)
#     print(arr)
#     IPS+=arr
#
# with open("IPS.txt",'wb') as f:
#     pickle.dump(IPS,f)

# 测试代理ip
# with open("IPS.txt",'rb') as f:
#     arr=pickle.load(f)
#
# IPS = [] # 可用代理IP
# 单线程
# #
# def test(ip):
#     proxie = {
#         'http':'http://%s'%ip,
#         'https':'https://%s'%ip,
#     }
#     try:
#         with requests.get('https://www.baidu.com',proxies=proxie,timeout=5) as res:
#             print("ok %s可用"%ip)
#             with open("ipok.txt", 'a') as f:
#                 f.write(ip+"\n")
#     except Exception:
#         print('error %s不可用'%ip)
# #
# for ip in arr:
#     test(ip)
#

ua = UserAgent()
# # requests 包中利用cookie以及session来实现登录
# login = "http://118.190.150.35:9000/login"
#
# header = {
#     'User-Agent':ua.random
# }
# data = {
#     'username':'',
#     'password':''
# }
#
# # res = requests.post(login,data=data,headers=header)
#
# session = requests.session()  # session对象
# res0 = session.post(login,data=data)
#
# login = "http://118.190.150.35:9000/login"
#
# res = session.get(login)
#
# ribao = 'http://118.190.150.35:9000/uektrain/daily/uekDailyStudent/viewAfterDailyByClass?date=2019-04-02&classId=145&dailyId=0a577fcb3ea745c892a1a7983e5c47b0&isfillup=0&studentId=2089'
#
#
#
# print(res.text)
# print(res.url)
# # print(res.status_code)
#
#
# URL = "http://118.190.150.35:9000/uektrain/daily/uekDailyStudent/updatecontent"
# login = "http://118.190.150.35:9000/login"
# ribao = {
#     'uekDailyStudentDO.id':'24749561da5844b0b59896f43372e068', # 学生id
#     'uekDailyStudentDO.motto':'好好学习天天向上', # 座右铭
#     'uekDailyStudentContentDO[0].workContent': "爬虫", #工作内容
#     'uekDailyStudentContentDO[0].completeness':'100', #完成情况
#     'uekDailyStudentContentDO[0].poblem':'无', # 问题
#     'uekDailyStudentDO.mood':'好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上好好学习天天向上'# 工作内容
# }
# header = {
#     'User-Agent':ua.random
# }
# data = {
#     'username':'15835007400',
#     'password':'111111'
# }
#
# sess = requests.session()
# sess.post(login,data=data)
# res = sess.post(URL,data=ribao)
# print(res.text)
# # print(res.status_code)
#



