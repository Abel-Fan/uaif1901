#Scrapy中间件
"""
Scrapy爬虫框架
items.py  字段
spider
    douban.py  自己的爬虫文件，自己的爬虫规则
    parse文件 会在一开始被Request(url,callback=parse)对象所调用
    def parse(self,response):
        response # 响应  类型：textResponse(Response子类)
        方法：
            xpath()
            css()
        xpath,css返回selection对象
        selection对象方法
            extract() #获取文本
            re()  #通过正则获取文本
    非常有可能遇到 请求列表 请求详情
        meta = {'myData':[1,2,3]}
        yield Scrapy.Request(url,[,headers][,meta][,methods],callback=self.getList)

    def getList(self,response):
        response.meta['myData']

    settings.py 爬虫设置文件
    请求头，代理池，对爬虫的设置。开启管道，开启中间件 ，
    限制爬取时间，几个线程爬取...

    pipelines.py 管道文件
    爬虫文件中，要么返回item对象，要么返回Requests()对象
    只要返回item对象，在pipelines.py就能接收
    数据清洗、数据保存:过滤、去重、存储

    middlewares.py 中间件

    爬虫整体架构

                  调度器       （引擎->下载器  请求前）IP代理 User-Agent随机 Ajax数据处理
            管道   引擎      下载中间件     下载器
                                （下载器->引擎 响应 ）
                爬虫中间件
                  爬虫文件

    class MyMiddle1(下载中间键):
        def processrequest():
            会在请求前执行
        def processresponse():
            会在响应后执行
        def processexception():
            出错后执行的内容
    class MyMiddle2(下载中间键):
        def processrequest():
            会在请求前执行
        def processresponse():
            会在响应后执行
        def processexception():
            出错后执行的内容
    class MyMiddle3(下载中间键):
        def processrequest():
            会在请求前执行
        def processresponse():
            会在响应后执行
        def processexception():
            出错后执行的内容
"""


# 线程
# 同步机制
from threading import Thread,Semaphore,BoundedSemaphore,Event,Barrier
"""
semaphore(value) 信号量对象  主要功能限制线程数量。
方法: acquire()  release()
BoundedSemaphore  与semaphore区别  
semaphore 释放超出不会报错
BoundedSemaphore 会报错


Event 事件锁 主要功能是线程运行或阻塞由另外的主线程所决定
在内部保存了flag  可以通过 set开启flag 可以通过clear方法 关闭flag
方法
wait() 
set()
clear()
isSet()

Barrier 栅栏 主要功能是可以实现线程并行
Barrier(num) 冲出栅栏所需线程数量
num=10 线程为10才运行 否则阻塞
方法：
wait()
reset() 重置栅栏
abort() 使栅栏破损，可能会出现死锁时使用
broken  栅栏是否破损
n_waiting  栅栏中正在阻塞的线程数量
parties = num 冲出栅栏所需线程数量


queue 对列是一种数据结构，默认是先入先出类似管道。内部实现了锁机制
queue.Queue(num) 先入先出队列
queue.LifoQueue(num) 后入先出队列
queue.PriorityQueue 优先级队列 实现了队列排序

get()
put(item)
get_nowait()
put_nowait()
empty() 是否为空 
qsize() 队列大小
full() 是否为满

task_done() 任务完成信号
join()  阻塞主线程直到所有元素处理完毕
  
"""

