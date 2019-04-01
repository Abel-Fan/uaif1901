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
