# 异常
"""
try:
    #可能会发生异常的代码

except 异常类 as e:
    #出现异常执行的代码
except 异常类2 as e:
    pass
else:
    没有发生异常执行的代码
finally:
    无论是否发生异常 都要执行的代码

"""
"""
# 自定义异常
class myError(Exception):
    def __init__(self,info):
        super().__init__(self)
        self.info = info
    def __str__(self)
        return self.info
"""

"""
#抛出异常
raise  myError 
"""

# 模块与包
# 模块：python脚本文件
# 包： 模块的集合
# 包类似于文件夹  模块相当于文件
# 分类 ：正规包 命名空间包
# 正规包: 文件夹中包含 __init__.py文件
# 命名空间包： 不包含__init__.py文件
# 正规包与命名空间包区别：命名空间包不受物理位置限制
# 包的导入顺序
# re.py  先从当前目录寻找包，然后从系统路径中寻找
# sys.path 列表数据 保存的寻址路径，可以添加自己的路径

#导入包的方式
# from  import as *
# 在非主运行包中 可以使用 相对路径的方式导入  . 当前  .. 上一级

# __main__ 可以是包直接运行