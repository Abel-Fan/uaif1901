# Scrapy
# 安装
# 1、pywin32  http://sourceforge.net/projects/pywin32/ 选择对应版本
# 2、Twisted
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
# 把下载文件放在项目中，  pip install Twisted-18.9.0-cp37-cp37m-win32.whl
# 3、pip install Scrapy

# 步骤
# 1、创建项目
# scrapy startproject 项目名称
# 2、增加 items.py  创建数据模型
# 3、创建爬虫文件
# scrapy genspider 爬虫名字  站点
# 4、运行
# scrapy crawl 爬虫名称