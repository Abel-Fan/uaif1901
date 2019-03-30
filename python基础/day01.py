# python 动态类型、强类型语言。

# 输入工具
# input获取的数据都是字符串类型

# string = input("请输入你的名字")
# print(type(string))

# 输出工具
# print("123")
# print("123","456",end="")
# print("123",456,1+2)

# 格式化输出
# print("我叫%s,我的年龄是%d,我的数学成绩%0.2f"%('horns',19,56.05))
# print("我叫%s"%'horns')

# 转义
# print("n\nn")
# 前缀
# r 后面的字符串都是普通字符串 类似于Linux ''
# print(r"n\nn")
# b 后面的字符串都是byte
# u 后面的字符串都是unicode

# 变量
# 变量的定义
# python赋值变量
# 1普通
# a = 10
# 2链式
# b=c=d=20
# 3多元
# e,f=10,20
# # 交换
# e,f = f,e
#
# print(e,f)

# 变量命名特点
# 1、不可以是关键字和保留字
# 2、汉字数字字母下划线 数字不能开头
# 3、语义化
# 4、严格区分大小写
# 5、不能使用特殊符号

# 杨登辉 = 1234
# print(杨登辉)
# a = 10
# A = 20
# print(a,A)


# js : 数字 字符串 布尔 null undefined object
# python: 数字 字符串 布尔 None
#    列表（数组）元组 字典（object\json）集合
# js分类 基本数据类型和引用数据类型
# python分类 可变数据类型和不可变数据类型 （全部是引用数据类型）
# 可变数据类型：列表、字典、集合
# 布尔  True False
# 数字 整型、浮点型（数字精度）
# 字符串
# ''  ""   ''''''  """"""
# str1 = 'abc'
# str2 = "def"
# str3 = '''g
#
# hi'''
# print(str1,str2,str3)

"""
abcdef  注释
"""
'''
块级注释
'''

# 切片
# a = "山西优逸客科技有限公司"
# 切片功能
# print(a[2:5])
# 语法
# string[start:end:step]  [初始值:结束前:步进值]
# 每个值可以为负或空（默认）
# start == 开始（前开始、后开始）
# end == 结尾(前结尾、后结尾)
# 步进值  == 1 如果为-1改变方向
# print(a[::-1])
# print(dir(a))

# 列表
# arr = [[1,2],[3,4]]
# 访问列表
# print(arr[-1])
# 获取列表长度
# print(len(arr))
# 深拷贝浅拷贝
# arr1 = arr  #传址

# print(id(arr1),id(arr))
# arr1[0] = 'a'
# print(arr1)
# print(arr)
# import copy
# arr1 = copy.deepcopy(arr) # 浅拷贝
# arr1[0][0] = 'a'
# print("arr1",id(arr1),arr1)
# print("arr",id(arr),arr)
# arr1 = arr.copy()  # 浅拷贝

# 遍历
# 1
# for item in arr:
#     print(arr.index(item),item)
# 2
# range()
# 1个参数：结束的值。返回 包含0 - n之前的数的序列
# print(list(range(10)))
# 2个参数：开始的位置，结束的位置。返回包含开始-结束 之间的数的序列
# print(list(range(5,10)))
# 3个参数：开始，结束，步进值

# for i in range(len(arr)):
#     print(i,arr[i])

# 3
# enumerate() 返回列表元素
# print(list(enumerate(arr))
# for i,v in enumerate(arr):
#     print(i,v)
# a,b,c,d,e = (1,2,3,4,5)

# 列表推导式推导式
# 快速生成新的列表
# 推导式
# 列表推导式、字典推导式、集合推导式

#列表推导式
# arr = [1,2,3,4,5]
# 语法：
# 1 每个元素幂运算
# arr2 = [ item*item for item in arr ]
# print(arr2)
# 2 输出偶数 ,并且幂运算
# arr2 = [ item*item for item in arr if item%2==0 ]
# print(arr2)


# 元组
# 定义：不可改变的列表
# 语法：
# t1 = ()
# print(type(t1))
# t2 = (1,)
# print(type(t2))
# 面试题
# t1=([1,2],[3,4])
# t1[0][0] = 2
# print(t1)

# 字典 （对象，json）
# 语法
# （1）json方式
# dict1 = {1:123,'name':'horns',(1,2,3):'abc'}
# 访问
# print(dict1[1])
# print(dict1['name'])
# print(dict1[(1,2,3)])
#字典的键需要进行hash运算，只要键能进行hash（哈希）运算就可以设置，可变数据类型不可以哈希运算
# 通过dict()内建函数创建
# （2）dict2 = dict() # 创建了空的字典
# 设置键值
# dict2[1] = 123
# dict2['name'] = 'horns'
# dict2[(1,2,3)] = 'abc'
# print(dict2)

# 批量创建键值
# dict3 = dict.fromkeys([1,2,3,4,5],'a')
# print(dict3)

# 删除字典的数据以及字典  del
# del dict3[2]
# print(dict3)
# del dict3
# print(dict3)

# 遍历字典
# 1
# for k in dict3:
#     print(k)
#     print(dict3[k])

# 2
# print(dict3.items())
# for k,v in dict3.items():
#     print(k,v)

# 3
# arr = zip([1,2,3,4],['a','b','c','d'],[11,22,33,44])  # 将传入的列表一一对应
# print(list(arr))
# dict3.keys() # 返回键
# dict3.values() # 返回值
#
# for k,v in zip(dict3.keys(),dict3.values()):
#     print(k,v)
d = {'a':1,'A':10,'b':2,'B':20}
# 字典推导式
# 1
# d2 = { k:str(v)+'m' for k,v in d.items() }
# print(d2)
# 2
# d3 = { k:str(v + d[k.upper()])+'px' for k,v in d.items() if k.islower()}
# # print(d3)

# 其他内建函数
# d.get()
# d.pop()
# d.clear()
# d.setdefault()
# in & not in
# d.update({'c':3,'C':30})
# d.setdefault('d',"333")
# print(d)

#集合
s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# # 集合操作
# # 交集
# print(s1&s2)
# # 并集
# print(s1|s2)
# # 差集
# print(s1^s2)

# 集合推导式
# 1
# s2 = { item+1 for item in s1}
# print(s2)
# 2
# s2 = {item for item in s1 if item%2==0}
# print(s2)
# 通过集合元素没有重复这一特点进行列表的去重
# arr1 = [1,1,2,2,3,4,2,2,5,9,8,6,8,4,3]
# print(list(set(arr1)))

# arr1.sort(reverse=True)
# arr1.reverse()
# print(arr1)
