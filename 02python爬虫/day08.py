# selenium
# (https://selenium-python-zh.readthedocs.io/en/latest/installation.html)
# 安装  pip install selenium
# 安装  chromedriver  (http://npm.taobao.org/mirrors/chromedriver/)
# 概述： selenium 浏览器测试工具，主要用作与测试web应用

from selenium import webdriver
from selenium.webdriver.common.by import By  #获取元素
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 条件
from selenium.webdriver import ActionChains
import requests
import time


# driver = webdriver.Chrome(r"C:\Users\yangd\AppData\Local\Google\Chrome\Application\chromedriver.exe")
#
# driver.get("http://118.190.150.35:9000/login")
# time.sleep(2)
#
# username = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")
#
# username.send_keys("yangdenghui")
# password.send_keys("yangfan.")
#
# loginbtn = driver.find_element_by_partial_link_text("登")
#
# action = ActionChains(driver)
# action.click(loginbtn).perform()
# time.sleep(3)
# look = driver.find_element_by_css_selector(".J_menuItem")
# span = driver.find_element_by_css_selector("a span.nav-label")
#
# action2 = ActionChains(driver)
# action2.click(span).pause(1).click(look).perform()
#
# time.sleep(10)
# driver.close()

#
# url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%BF%90%E5%9F%8E'
# driver = webdriver.Chrome(r"C:\Users\yangd\AppData\Local\Google\Chrome\Application\chromedriver.exe")

# 隐式等待
# driver.get(url)
# driver.implicitly_wait(5)
# td = driver.find_element_by_class_name("hidden-xs")
# print(td)
# with open("yuncheng.html",'w',encoding='utf8') as f:
#     f.write(driver.page_source)
#
# print(driver.page_source)

# 显示等待
# driver.get(url)
#
#
# WebDriverWait(driver,10).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME,'hidden-xs'))
# )
#
# driver.close()

#
# url = 'https://unsplash.com/t/wallpapers'
# driver = webdriver.Chrome(r"C:\Users\yangd\AppData\Local\Google\Chrome\Application\chromedriver.exe")
#
# driver.get(url)
# driver.execute_script("window.scrollTo(0,2000)")
#
# time.sleep(5)
# with open("img.html",'w',encoding='utf8') as f:
#     f.write(driver.page_source)
#
# driver.save_screenshot("img.png")
# driver.close()

# 正则表达式
# 正则概述
# 一、正则表达式 二、re模块
#
import re
# res = re.search()
# res = re.findall("c","abc123bcd") #查找

# 元字符
# \w 字符
# \W 非字符
# \d 数字
# \D 非数字
# \b 单词边界
# \B 非单词边界
# \s 空
# \S 非空
# .所有字符除了\n

# 原子表
# []
# [abc]
# [a-z]
# [A-Z]
# [1-9]
# [a-zA-Z1-9]
# [^...] 取反

# 数量
# *  0个或多个
# +  1个或多个
# ?  0个或1个
# {n} n个
# {n,} n个或多个
# {n,m} n个到m个


res = re.findall(r"\w{2,}","abcdefg")

# 匹配qq号码（5位-10位）
list1 = [
    1234245,
    12523462345,
    143623452341,
    25145,
    1251346,
    1324,
    123556,
    12324657869,
    123434,
]

# qq邮箱验证
#
# email = re.search(r"^\d{5,10}@qq.com$",'842615663@qq.com')
# email2 = re.search(r"^[a-zA-Z]\w*@163.com$",'yangdenghui123@163.com')
# email3 = re.search(r"^[\w]+@(qq|163|139).(com|cn)$",'yangdenghui123@163.com')
# print(email3.group())
# # 电话号码验证
#
# # res1 = re.search('^\d{5,10}$',str(list1[2]))
# # print(res1)
# list2 = [item for item in list1 if re.search(r'^\d{5,10}$',str(item))]
# print(list2)

# 身份证
#  15 18 xX
# res4 = re.search(r'^\d{15}$|^\d{17}[1-9xX]$','12343747586958482x')
# print(res4.group())

# () 组
# (?P<name>) 命名组，定义组
# 正则表达式中调用  (?P=name)  \1 \2..
# 正则对象中 res.group(n)  res.groupdict()


# res5 = re.search(r'<(?P<tag>\w+)>(?P<con>.*)</(?P=tag)>','<div>this is div</div>')
# res5 = re.search(r'<(?P<tag>\w+)>(?P<con>.*)</(\1)>','<div>this is div</div>')
# print(res5.group(3))

# rege = re.compile("[;,.]") # 正则表达式
#
# res5 = rege.split("a;b,c.d")


# sub()
# def fn(a):
#
#     res = str(int(a.group())*2)
#     return res
#
# res5 = re.sub("\d+",fn,"山西优逸客 就业人数1000 高薪就业900")
#
#
# print(res5)

# 模式
# rege = re.compile("""[a-z] #字母""",re.X)
# res6 = rege.findall("""
# asdlfjejtoqjwer
# asdfasdf
#
# """)
# print(res6)

#<div class='asdfakg'>运城</div> <td>温度</td>
