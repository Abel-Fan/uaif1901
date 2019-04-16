# 回顾
# 系统编程
# 多线程（IO密集型程序）
# threading
# 常用的组件： Thread Lock RLock condition ...
# 一、threading常用函数
import threading
"""
threading.active_count()  # 活动线程数量
threading.activeCount()
threading.current_thread() # 获取当前活动线程对象
threading.currentThread()
threading.enumerate() # 获取所有活动线程
threading.get_ident() # 获取当前线程标识符
threading.stack_size(>=32*1024)
threading.main_thread() # 获取主线程
"""
# 二、Thread线程模块
# 1、创建线程
#   构造函数  继承Thread类
def fun():
    print(123)
t = threading.Thread(target=fun,args=())
# 2、Thread对象方法
"""
t.start()  # 运行线程， 调用了线程对象的run方法
t.join()  # 阻塞主线程
t.is_alive() # 是否为活动线程
t.isAlive()
t.name   #获取或设置线程名，默认Thread-num
t.getName()  #获取线程名
t.setName() #设置线程名
t.daemon # 是否为守护线程，True为守护线程，默认为False
t.setDaemon() # 设置主线程
t.ident  #线程标识符
"""
# 二、Lock 原始锁
# 1、创建锁
l = threading.Lock()
# 2、方法
# l.acquire(
#       blocking=True, # 是否阻塞
#       timeout=-1   # 超时时间
#       )   #获取锁
# l.release() # 释放锁
# 3、死锁
# 4、注意：获取锁和释放锁必须一一对应，如果release 多于 acquire 报错

# RLock 递归锁,重复锁,局部锁
# 1、定义
"""
rlock = threading.RLock()
def fun1():
    rlock.acquire()
    rlock.acquire()
    print('fun1')
    rlock.release()
    rlock.release()
def fun2():
    rlock.acquire()
    rlock.acquire()
    print('fun2')

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
"""

# condition 条件锁,基于RLock
# 1、定义
con = threading.Condition()
# 2、方法
"""
con.acquire()
con.release()
con.wait()  # 释放锁，并且阻塞
con.notify(n=1) # 通知其他线程 n为数量
con.notify_all()  # 通知所有线程
con.wait_for(predicate=fun(),timeout=-1)
"""
# import time
# print("主线程开始")
# def fun():
#     time.sleep(2)
#     return True
# con.wait_for(fun)   # 阻塞，直到 predicate 返回True
# print("主线程结束..")
#

# 信号量对象
# Semphore，是一种带计数的线程同步机制，当调用release时，增加计数，当acquire时，减少计数，当计数为0时，自动阻塞，等待release被调用。

# from threading import Thread,Semaphore
# import time,random
#
# sem = Semaphore(10) # 班级
# num = 0  # 人数
# students = []
#
# class Consumer(Thread):
#     def __init__(self,sem):
#         super().__init__()
#         self.sem = sem
#     def run(self):
#         time.sleep(random.randint(3,10))
#         print("结训一人")
#         global  num
#         num-=1
#         self.sem.release()
#
# class Produces(Thread):
#     def __init__(self):  # 招生
#         super().__init__()
#     def run(self):
#         global num
#         sem.acquire()
#         num+=1
#         print("班级人数:%s"%num)
#         t = Consumer(sem)
#         t.start()
#
# for i in range(20):
#     t = Produces()
#     t.start()


# Event  直行红灯
# from threading import Event,Thread
# import time
#
# event = Event()
# event.clear() # 将Event开关设置为False
# """
# event.set()  将开关设置为True
# event.isSet()  查看开关是否为True
# event.wait([timeout]) 等待
# """
# num = 4
#
# class RedGreen(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         while True:
#             global num, flag
#             time.sleep(1)
#             num -= 1
#
#             print("倒计时:%s"%num)
#             if num==0:
#                 event.set()
#                 time.sleep(2)
#                 event.clear()
#             if num<=0:
#                 num=4
#
#
#
# class Car(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         while True:
#             if event.isSet():
#                 time.sleep(2)
#                 print("%s:直行通过红路灯"%self.name)
#             else:
#                 event.wait()
#
# t1 = RedGreen()
# t1.start()
#
# for i in range(5):
#     c = Car()
#     c.start()

# 栅栏
from threading import Thread,Barrier
import time,random

def fun():
    print("<比赛开始>")

bar = Barrier(10,action=fun)

"""
parties 栅栏打开所需线程数量
n_waiting 当前正在栅栏中阻塞的线程
wait() 等待
rest() 重置栅栏
abort() 使栅栏破损
broken 一个布尔值为True表示栅栏受损
"""
# 田径比赛
#
# class Per(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         time.sleep(1)
#         print("%s已经准备好了..."%self.name)
#         bar.wait()
#         time.sleep(random.randint(2,5))
#         print("%s跑完了全程"%self.name)
#
# for i in range(10):
#     p = Per()
#     p.start()


# Lock 、 RLock 、 Condition 、 Semaphore 和 BoundedSemaphore 对象可以用作 with 语句的上下文管理器。

# import threading
# lock = threading.Lock()
#
# def fun(num):
#     with lock as l:
#         time.sleep(1)
#         print(num)
#
# for i in range(10):
#     t = threading.Thread(target=fun,args=(i,))
#     t.start()


from queue import Queue,LifoQueue,PriorityQueue
"""
队列 是一种数据结构
Queue FiFo  先入先出
LiFoQueue LiFo 后入先出 
PriorityQueue 优先级队列
"""
import random

# q = Queue(10)
# q= LifoQueue(10)
# q = PriorityQueue(10)
# arr = ['1','10','90','30','a']
# for i in range(10):
#     q.put(random.choice(arr))
#
#
# for i in range(10):
#     print(q.get())

# q = Queue(10)
#
# class Produce(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         while True:
#             if not q.full():
#                 time.sleep(1)
#                 q.put("%s放的鱼丸"%self.name)
#                 print("%s放了鱼丸"%self.name)
#
# class Consumer(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         while True:
#             if not q.empty():
#                 time.sleep(2)
#                 yw = q.get()
#                 print("%s吃了%s"%(self.name,yw))
#
# for i in range(10):
#     p = Produce()
#     p.start()
#     c = Consumer()
#     c.start()
