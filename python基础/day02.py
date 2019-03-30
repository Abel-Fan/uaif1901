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