# 面向对象

# 类变量、实例变量
# 静态方法 类方法 实例方法

"""
类变量： 定义在类中，可以被类方法（修改），可以被实例访问
类方法：通过@classmethod装饰，修改类变量
静态方法：不依赖于类变量，类方法，实例变量，实例方法。
"""
#
# class P:
#     sex = '男'  # 类变量 ，能够被实例继承
#
#     def __init__(self):
#         self.name = 'xm'  # 实例属性，实例变量
#
#     @classmethod
#     def setSex(cls,sex):
#         cls.sex = sex
#
#     def say1(self):  # 实例方法
#         print(self.name)
#         print(self.sex)
#
#     @staticmethod
#     def say2():
#         print("this is static")
#
#
# xm = P()
# print(xm.sex)  # xm.sex 继承的类变量
# P.setSex('女') # 调用类方法 修改类变量
# print(xm.sex)
# xm.setSex('男') # xm这个实例 调用了继承的类方法修改了类变量
# print(xm.sex)
# xm.sex = "女"   #  添加了实例属性sex覆盖了类变量sex,并没有修改类变量
# print(xm.sex)
# print(P.sex)

#私有属性和私有方法
# 所谓私有，就是在外部不能调用，方法之间可以使用的
# 私有方法以及属性需要在方法名或属性名前加 "__"
# 但是python没有正真的私有方法私有属性。
# class P:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def say(self):
#         print('my name is %s'%self.__name)

# p = P('小红',19)
# print(dir(p))
# p._P__name = "小宏"
# p.say()


# @property 私有
# 将方法改成一个同名的属性(不能修改).
# class P:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def say(self):
#         print('my name is %s'%self.__name)
#     @property
#     def name(self):
#         return self.__name
#
# p = P('小红',19)
# print(dir(p))
# print(p.name)

# 继承与多重继承
#
# class Y:
#     def __init__(self):
#         self.gj = "石头"
#     def run(self):
#         print("直立行走")
#
# class P(Y):
#     def __init__(self):
#         super().__init__()
#         # super()用来引用父类而不必显式地指定它们的名称
#         self.yf = ""
#     def say(self):
#         print("沟通交流")
#
# p1 = P()
#
# print(dir(p1))
# print(p1.gj)

# 继承 调用 从左至右查找方法.

# class Car:
#     def __init__(self):
#         self.pp = ""
#         self.color = ""
#     def run(self):
#         print("启动")
#
# class ft:
#     def __init__(self):
#         self.type = ""
#     def run1(self):
#         print("丰田启动")
#
#
# class hg(ft,Car):
#     def __init__(self):
#         super(hg, self).__init__()
#         self.price = ""
#
# hg1 = hg()
# print(dir(hg1))
# hg1.run()

# 深度优先
# class A:
#     def __init__(self):
#         pass
#     def run(self):
#         print("A")
#
#
# class B:
#     def __init__(self):
#         pass
#     def run(self):
#         print("B")
#
#
# class C(A):
#     def __init__(self):
#         pass
#     def say(self):
#         print("C")
#
# class D(B):
#     def __init__(self):
#         pass
#     def say(self):
#         print("D")
#     def run(self):
#         print("D->run")
#
# class F(C,D):
#     def __init__(self):
#         pass
#
#
# f = F()
# # f.say()
# f.run()  #


#魔法方法

# （1）__slots__ 限制属性和方法
#
# class P:
#     """
#     Peron类  人类
#     """
#     def __int__(self):
#         pass
#     __slots__ = ['name','sex']
#     __name__ = "Person"
#     def run(self):
#         print(self.__doc__)
#
#
# p = P()
# p.name = 'horns'
# p.sex = '男'
# print(dir(p))
# print(p.__doc__)
#
# def fn():
#     """
#     this is fn
#     :return:
#     """
#     pass
#
#
# print(fn.__doc__)

#
# class Car:
#     def __init__(self):
#         self.color = ""
#
# class BWM(Car):
#     def __new__(cls, *args, **kwargs): # 创建实例，必须有返回值
#         print("new")
#         return super().__new__(cls)
#     def __init__(self):
#         print("init")
#         self.pingpai = ''
#     def __del__(self):
#         print("del")
#
# b = BWM()
# # del b
# del b
# print(b)
#
# # __new__ 与 __init__ 关系

import time

def sumtime(fn):
    def newFn(self,*args,**kwargs):
        start = time.time()
        fn(self,*args,**kwargs)
        end = time.time()
        print("%s你好帅"%self.name)
        print("总时间:%s"%(end-start))
    return newFn

# 类装饰器
class P:
    def __init__(self,name):
        self.name= name
    @sumtime
    def run(self):
        time.sleep(1)
        print(self.name)

# 实例方法装饰器


p = P("horns")
p.run()



