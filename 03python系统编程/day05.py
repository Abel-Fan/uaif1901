# 回顾
# 进程之间交换数据
# Queue、Pipe、Array、Value
# 进程池 Pool apply apply_async map map_async
# Manager() list dict Array Value Lock RLock
# multiprocess Lock RLock..
# socket套接字

# 协程
# 实现协程四种方式

# yield
# import time
# arr = []
# def Produce(gobj,name):
#     gobj.send(None)
#     for i in range(1,101):
#         time.sleep(1)
#         arr.append(i)
#         print("%s放了第%s个鱼丸，锅里还有%s个鱼丸"%(name,i,len(arr)))
#         if len(arr)>=5:
#             gobj.send(i)
# # 生成器
# def Consumer(name):
#     while True:
#         i = yield
#         time.sleep(1)
#         arr.pop()
#         print("%s吃了第%s个鱼丸，锅内还剩%s个鱼丸"%(name,i,len(arr)))
#
# gobj = Consumer("小红")
# Produce(gobj,"小白")


# greenlet

# from greenlet import greenlet
#
# def fun1():
#     print("白日依山尽")
#     f2.switch()
#     print("欲穷千里目")
#     f2.switch()
#
# def fun2():
#     print("黄河入海流")
#     f1.switch()
#     print("更上一层楼")
#
# f1 = greenlet(fun1)  # 任务对象
# f2 = greenlet(fun2)
# f1.switch()


# import gevent
# from greenlet import greenlet
#
# def fun1():
#     gevent.sleep(1)
#     print("窗前明月光")
#     gevent.sleep(5)
#     print("举头望明月")
#
# def fun2():
#     gevent.sleep(2)
#     print("疑似地上霜")
#     gevent.sleep(6)
#     print("低头思故乡")
#
# # gevent 创建任务
# t1 = gevent.spawn(fun1)
# t2 = gevent.spawn(fun2)
# gevent.joinall([t1,t2])

# import gevent
# from gevent import monkey
# monkey.patch_all()
# import requests
#
# urls = [ "https://movie.douban.com/top250?start="+str(i) for i in range(0,251,25)]
#
# def getRes(url):
#     print("正在请求%s"%url)
#     res = requests.get(url)
#     print(res.text)
#
# arr = []
# for link in urls:
#     arr.append(gevent.spawn(getRes,url=link))
#
# gevent.joinall(arr)
#
# import asyncio,time
#
# async def fun1():
#     await asyncio.sleep(1) # 编程可等待对象
#     print(123)
# async def fun2():
#     await asyncio.sleep(2)
#     print(456)
# async def fun3():
#     await asyncio.sleep(3)
#     print(789)
#
# async def main():
#     # await fun1()
#     # await fun2()
#     # await fun3()
#     t1 = asyncio.create_task(fun1())
#     t2 = asyncio.create_task(fun2())
#     t3 = asyncio.create_task(fun3())
#     await asyncio.gather(t1,t2,t3)
# # asyncio.create_task(fun1())
# start = time.time()
# asyncio.run(main())
# end = time.time()
# print("运行总时间:%s"%(end-start))

import asyncio,time

# async def fun1():
#     await asyncio.sleep(1)
#     print(123)
#
# async def fun2():
#     await asyncio.sleep(2)
#     print(456)
#
# async def fun3():
#     await asyncio.sleep(3)
#     print(789)
#
# async def main():
#     # await fun1()
#     # await fun2()
#     # await fun3()
#     t1 = asyncio.create_task(fun1())
#     t2 = asyncio.create_task(fun2())
#     t3 = asyncio.create_task(fun3())
#     await asyncio.gather(t1,t2,t3)
# 调用第一种方式
# asyncio.run(main())

# 调用第二种方式  await + asyncio.run()
# start = time.time()
# asyncio.run(main())
# end = time.time()
# print("运行总时间：%s"%(end-start))

# 并发运行 asyncio.create_task() + asyncio.gather(t1,t2,t3)

# start = time.time()
# asyncio.run(main())
# end = time.time()
# print("运行总时间：%s"%(end-start))
arr = []
async def prduces():
    for i in range(100):
        await asyncio.sleep(1)
        arr.append(i)
        print("小明，放了一个鱼丸,锅内还有%s"%(len(arr)))

async def consumer():
    while True:
        await asyncio.sleep(0)
        if len(arr)>5:
            await asyncio.sleep(2)
            arr.pop()
            print("小红，吃一个鱼丸,锅内还有%s" % (len(arr)))

async def main():

    t1 = asyncio.create_task(prduces())
    t2 = asyncio.create_task(consumer())
    await asyncio.gather(t1,t2)

asyncio.run(main())
