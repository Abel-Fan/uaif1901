import time,datetime
# python中时间的三种形式
# 1、时间戳
# print(time.time())
# 2、时间元组
# print(time.localtime())
# print(time.localtime().tm_year)
# 3、格式化时间字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# print(time.mktime(time.localtime()))
# dateobj = datetime.date(2018,8,8)
# print(datetime.date.today())
# print(datetime.date.fromtimestamp(time.time()))
# print(dateobj.replace(day=28))


# timeobj = datetime.time(11,23,30)
# print(timeobj.strftime("%H-%M-%S"))
# timeobj.replace(hour=,minute=,second=)


datetimeobj = datetime.datetime(2019,4,30,12,0,0)
# print(datetimeobj)
# datetimeobj.strftime("")

obj = datetime.timedelta(days=4)
print(datetimeobj+obj)
