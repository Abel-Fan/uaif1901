# 函数装饰器
# 给某一个函数或程序增加新的功能
# 三个条件
# 1、不能更改原函数
# 2、不能更改原函数的调用方式
# 3、满足 1、2
import time



# fn()
# 新功能：输出运行总时间
# 方式一
# def fn2(fn):
#     def newFn(*args,**kwargs):
#         start = time.time()
#         fn(*args,**kwargs)
#         end = time.time()
#         print("总时间：%s"%(end-start))
#     return newFn
# fn = fn2(fn)
# fn()

# 方式二：装饰器语法
# @fn2
# def fn():
#     time.sleep(1)
#     print("end..")
#
# @fn2
# def fn1():
#     print("abc")
#
# fn()
#
# fn1()

# <函数+实参高阶函数+返回值高阶函数+闭包函数+语法糖=装饰器>


# 原函数传参
# def fn2(fn):
#     def newFn(*args,**kwargs):
#         start = time.time()
#         fn(*args,**kwargs)
#         end = time.time()
#         print("总时间：%s"%(end-start))
#     return newFn
# @fn2
# def fn(name):
#     time.sleep(1)
#     print("my name is %s"%name)
# fn("horns")


# 装饰器传参

# def fn2(funName):
#     def newFn(fn):
#         def newFn2(*args,**kwargs):
#             print("装饰（%s）函数"%funName)
#             start = time.time()
#             fn(*args,**kwargs)
#             end = time.time()
#             print("总时间：%s"%(end-start))
#         return newFn2
#     return newFn
#
# @fn2('fn函数')
# def fn(name):
#     time.sleep(1)
#     print("my name is %s"%name)
#
# fn("horns")


## 装饰器嵌套
"""
@fn2('fn2')
@fn1('fn1')
def fn():
    pass
"""
# 了解装饰器运行流程

# @fn1装饰器  输出装饰器的名字

# def fn1(funName1):
#     print("%s在执行"%funName1)
#     def newFun(fn):
#         def newFun2(*args,**kwargs):
#             print("%s在调用"%funName1)
#             fn(*args,**kwargs)
#         return newFun2
#     return newFun

#@fn2装饰器 输出装饰器的名字

# def fn2(funName2):
#     print("%s在执行" % funName2)
#     def newFun(fn):
#         def newFun2(*args,**kwargs):
#             print("%s在调用"%funName2)
#             fn(*args,**kwargs)
#         return newFun2
#     return newFun
#
# @fn2("@fun2")
# @fn1("@fun1")
# def fn(name):
#     print(name)
#
# fn("horns")

# 装饰器执行是按照从上到下执行的


#面向对象
# 一、概述
# 面向对象与面向过程
# 面向对象的特点： 封装、继承、多态
# 类：
# 对象：

# 语法
"""
class 类名(基类、父类):
    def __init__(self):  # self => this 实例
        # 实例属性  
        self.name='horns'   # __init__ => constructor
        self.age = 18
    # 实例方法
    def say(self):
        print(self.name)
"""



# 创建一个Person类
# class Person:
#     def __init__(self,name='horns',age=18):
#         self.name=name
#         self.age=age
#     def say(self):
#         print("my name is %s"%self.name)
# # 实例化，创建对象
# xm = Person('小明',17)
# xm.say()

# 创建钟表

# 属性 小时:分钟:秒钟
# 方法
# run 表跑起来
# set 设置时间
# print(obj)  输出 现在的时间

# class Clock:
#     def __init__(self,hou=0,min=0,sec=0):  # 魔法方法
#         self.hou = hou
#         self.min = min
#         self.sec = sec
#     def run(self):
#         while True:
#             print(self)
#             time.sleep(1)  # 阻塞
#             self.sec+=1
#             if self.sec>59:
#                 self.min+=1
#                 self.sec=0
#                 if self.min>59:
#                     self.hou+=1
#                     self.min=0
#                     if self.hou>23:
#                         self.hou=0
#     def __str__(self): # 对实例的描述  print(obj) 打印 __str__()魔法方法的返回值
#         return '%0.2d:%0.2d:%0.2d'%(self.hou,self.min,self.sec)
#
# c1 = Clock(14,41,20)
# c1.run()
