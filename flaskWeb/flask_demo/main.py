from flask import Flask
from flaskWeb.flask_demo.blue_print.index import indexblue
from flaskWeb.flask_demo.blue_print.admin import adminblue

app = Flask(__name__)
app.register_blueprint(indexblue)
app.register_blueprint(adminblue)

if __name__ == "__main__":
    app.run(debug=True)


# flask
# MVT
# M module 模型 代表数据
"""
数据库: mysql 关系型数据库
# 创建数据库 create database 数据库名字
# 使用数据库 use 数据库
# 创建表 create table 表名(
    字段1 约束
    ..
) charset=utf8

常用数据类型
int(11)
varchar(255)
timestamp 时间戳

数据查询语句
插入数据 insert into 表名 (字段1,字段2,..) values (值1,值2)
查询数据 select 字段1,字段2 from 表名 where 条件  limit 数量

pymysql
连接数据库
database = pymysql.connect(host=,port=,db=,user=,password=)
cursor = database.cursor()
cursor方法
cursor.execute('sql语句')
# 防止sql注入
原则不相信用户输入，不要拼接字符串。
cursor.execute('select * from users where username=%s',username)

cursor.fetchall() 查找全部
cursor.fetchone() 查找一个

database.commit() # 对数据进行了增加，修改，删除需要提交数据库。

ORM 对象关系映射（后面讲）

"""
# V view   视图 业务逻辑
"""
业务逻辑
涉及 请求、响应、数据库操作
"""
# T template 模板
"""
jinja语法

{% for item in data%}
{% endfor %}

{% if adsf %}

{% endif %}

"""
