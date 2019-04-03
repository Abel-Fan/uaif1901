# 运算符
# 一、算术运算符
#  + - * /    %  //地板除  **幂运算
# （1）+ 加法用法
# 1 算术运算
# 2 拼接 str list tuple
# print("str1"+"str2")
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))

# （2）* 乘法运算
# 用法同加法
# print('str1'*2)
# print([1,2]*2)
# print((1,2)*2)

# （3）/ 除法的运算结果都为浮点型
# print(10/5)

## （4）// 地板除 向下取整
# print(9//2)

# （5）** 幂运算
# print(2**3)


# 二、逻辑运算符
# and or not
# is 判断是否为同一个对象  is not
# is、==区分

# 面试题：
# arr1 = [1,2,3]
# arr2 = arr1
# print(arr1==arr2)
# print(arr1 is arr2)

# arr1 = [1,2,3]
# arr2 = [1,2,3]
# print(arr1==arr2)
# print(arr1 is arr2)

# a = 10
# b = a
# print(a==b)
# print(a is b)

# a = 10
# b = 10
# print(a==b)
# print(a is b)

#三、关系运算符
# < <= > >= != ==

# 位运算
# ~按位取反
# <<  左移
# >>  右移
# & 与运算
# | 或运算
# ^ 异或运算
# 二进制、八进值、十进制、十六进值
# print(0b10)
#FFFFFF
# FF
# F*16+F*16
#rgb(255,255,255)


# print(2<<2)

# 2<<1
# 10 -> 100  4
# print(2>>1)
# print(2&3)

# 10
# 11
# 10
# print(2|3)
# 10
# 11

# print(2^3)
# 10
# 11
# 01


# print(~2)
# print(~3)
# print(~4)
# 100

# 原码
# 反码
# 补码


# 五、赋值运算符
# = += -= *= /= %= //= **=
# a=10
# a/=5  # a= a/5
# print(a)
# a = 10
# a //= 3 # a =a//3
# print(a)
# a=2
# a**=3 # a=a**3
# print(a)

# 一元运算符
# del

# arr = [1,2,3]
# del arr
# print(arr)  # error

# 三元运算符
# a,b = 10,20
# print("a>b") if a>b else print("b>a")

# 流程控制
# 一、分支
# if
# a,b=10,20
#
# if a>b:
#     print("a>b")
# elif a==b:
#     print("a==b")
# else:
#     pass

# pass 占位
"""
if(a>b){
    
}
"""
# 二、循环
# (1) for
# range()序列
# for i in range(1,11):
#     print(i)

# (2) while
# a1,b1=10,20
# while a1<b1:
#     print(a1)
#     a1+=1
# for 与 while区别
# 是否明确循环次数
# (3)干预循环
# break continue

# 猜数字
# import random
# 作业：random 常用方法
# num1 = random.randint(1,100)

# while True:
#     num2 = int(input("请输入一个0~100之间的数：\n"))
#     if num2>num1:
#         print("数字过大")
#     elif num2==num1:
#         print("恭喜你猜对了")
#         break
#     else:
#         print("数字过小")

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(j,i,j*i),end=" ")
#     print("")

# 列表推导式

# print("\n".join( [ "".join([ '%s*%s=%s '%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))

# 列表转字符串
# arr2 = ['1','2','3','4']
# print(",".join(arr2))


# 函数
# 一、语法
"""
def 函数名(形参):
    函数体
    return [value]
"""
# 二、调用
# 函数名(实参)

# 三、参数形式
# （1）必选参数
# def fn(name):
#     print(name)
# fn()   # TypeError

# (2) 缺省参数(默认参数)
# def fn(name,sex='男'):
#     print(name,sex)
#
# fn('horns')
# 必选参数与默认参数的顺序不可调整
# def fn(sex='男',name):  # SyntaxError
#     print(name,sex)
#
# fn('horns')

# （3）可变参数
# def fn(name,sex='男',*cj):
#     print(name,sex,cj,type(cj))
#
# fn('horns','男',12,34,45)

# (4) 关键字参数
# def fn(name,sex='男',*cj,**attr):
#     print(name,sex,cj,attr)
#
# fn('horns','男',12,14,34,56,height=180,weight=140)

# 顺序 : 必选参数 、默认参数（缺省参数）、可变参数、关键字参数
# 特殊用法：万能参数
# def fn(*args,**kwargs):
#     print(args,kwargs)
#
# fn(12,3213,41324,name='asdf',age='18')

# 解构用法
# def fn(a,b,c,d):
#     print(a,b,c,d)
#
# arr = [1,2,3,4]
# fn(*arr)

# def fn(name,age,sex):
#     print(name,age,sex)
#
# dict1 = {'name':'horns','age':'18','sex':'男'}

# fn(**dict1)
# fn(name='horns',sex='男',age='18') # 使用键值形式可以不遵循顺序

# 二、return

# def fn():
#     return 1,2,3
# print(fn())  # 返回值不可以是多个，如果有多个返回值默认为是元组

# 高阶函数
# 分类：实参高阶函数、返回值高阶函数
# 一、普通写法
# 加法运算
# def fn(a,b,c):
#     return sum([a,b,c])
#
# print(fn(1,2,3))

# 二、柯里化写法
# def fn(a):
#     def fn1(b):
#         def fn2(c):
#             return a+b+c
#         return fn2
#     return fn1
#
# print(fn(10)(20)(30))

# 匿名函数 lambda

# 一、语法
# lambda 参数1,参数2,..:函数体

#调用
# （1）高阶函数中作为参数
# def fn1(a):
#     return lambda b: lambda c:a+b+c
# print(fn1(10)(20)(30))

# （2）自调用
# print((lambda a,b:a+b)(10,20))

# （3）赋值
# fn = lambda a,b:a+b
# print(fn(10,20))

# 作用域、全局变量、局部变量
# global 全局 nonlocal 不是局部
# a = 123
# def fn():
#     # global a = 456 # SyntaxError
#     global a
#     a=456
#     print(a)
#
# fn()
# print(a)
# a = 123
# def fn1():
#     a = 456
#     def fn2():
#         nonlocal a
#         a = 789
#         print(a)
#     fn2()
#     print(a)
#
# fn1()
# print(a)

# 闭包函数
"""
在一些语言中，在函数中可以（嵌套）定义另一个函数时，如果内部的函数引用了外部的函数的变量，则可能产生闭包。闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性。
"""
# 递归函数
"""
如果一个函数在内部不调用其它的函数，而是自己本身的话，这个函数就是递归函数。
"""
