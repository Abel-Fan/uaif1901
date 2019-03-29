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
a = "山西优逸客科技有限公司"
# 切片功能
# print(a[2:5])
# 语法
# string[start:end:step]  [初始值:结束前:步进值]
# 每个值可以为负或空（默认）
# start == 开始（前开始、后开始）
# end == 结尾(前结尾、后结尾)
# 步进值  == 1 如果为-1改变方向
# print(a[::-1])
print(dir(a))