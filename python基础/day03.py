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

def fn1(funName1):
    print("%s在执行"%funName1)
    def newFun(fn):
        def newFun2(*args,**kwargs):
            print("%s在调用"%funName1)
            fn(*args,**kwargs)
        return newFun2
    return newFun

#@fn2装饰器 输出装饰器的名字

def fn2(funName2):
    print("%s在执行" % funName2)
    def newFun(fn):
        def newFun2(*args,**kwargs):
            print("%s在调用"%funName2)
            fn(*args,**kwargs)
        return newFun2
    return newFun

@fn2("@fun2")
@fn1("@fun1")
def fn(name):
    print(name)

fn("horns")

# 装饰器执行是按照从上到下执行的
