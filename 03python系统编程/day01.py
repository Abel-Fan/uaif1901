import threading
import time
# 创建线程两种方式

# 方式一：
# def fun(num):
#     time.sleep(1)
#     print(num)
# def fun1(num):
#     time.sleep(10)
#     print(num)
#
# t1 = threading.Thread(target=fun,args=(1,),name='t1')
# t2 = threading.Thread(target=fun1,args=(2,),name='t2')
# t1.daemon = True
#
# t1.start()
# t1.join(0.5)
# print("end....")
#


"""
线程方法：
daemon 是否为守护线程 False
getName 获取线程名字
ident   线程的标识符
isAlive 是否为活动线程  is_alive
isDaemon 是否为守护线程
name 线程名字
start 线程运行
join([timeout])  阻塞主线程,timeout为最长等待时间
"""

# print(dir(threading))
# 方式二：
#
arr = []
# threads = []
# class myThread1(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         # print("myThread1",threading.current_thread())
#         for i in range(10):
#             time.sleep(1)
#             arr.append(i)
            # print(arr)
#
# class myThread2(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         for i in range(10):
#             arr.pop()
#             print(arr)
#
#
# t1 = myThread1()
# t2 = myThread2()
# t1.start()
# t1.join()
# t2.start()


# threading常用函数
"""
activeCount() 当前活动线程的数量
active_count()
currentThread() 当前Thread线程对象
current_thread() 
enumerate()  当前活动线程对象
get_ident()  获取当前线程标识符
main_thread()  主线程
stack_size([size]) 当前线程使用栈的大小， size 32k以上 32*1024  byte
"""
#
# t = myThread1()
# t.start()
# print(threading.active_count())
# threads1 = threading.enumerate()
# print(threading.current_thread())
# threading.stack_size(32*1024)
# print(threading.stack_size())


# threading 常用模块 Thread
"""
Lock 锁 
RLock  复用锁，递归锁
Semaphore 信号锁
Condition 条件锁
Event 事件锁
...
"""
# Lock 锁
# 方法
# acquire 上锁， 获取锁
# release 解锁， 释放锁

# 临界区 ：访问公共资源的程序片段
#
# mylist = []
# threads = []
# num = 0
#
# lock = threading.Lock()
#
# class MyThread(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         global num
#         lock.acquire()
#         num+=1
#         # 其他功能
#         time.sleep(0.0001)
#         mylist.append(num)
#         lock.release()
#         # 其他功能
#         time.sleep(1)
#
# for i in range(10):
#     t = MyThread()
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(mylist)

# lock 获取锁以及释放锁要一一对应
# lock = threading.Lock()
# 死锁
# lock.acquire()  # 将lock 状态调为 locked
# lock.acquire()  # lock 阻塞等待 lock被释放

# lock.release() # RuntimeError: release unlocked lock


#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
#
# num = 0
# mylist = []
#
# class myThread(threading.Thread):
#     def __init__(self,num):
#         super().__init__()
#         self.num = num
#
#     def run(self):
#         if self.num==1:
#             self.fun1()
#         else:
#             self.fun2()
#
#     def fun1(self):
#         lock1.acquire()
#         time.sleep(0.5)
#         lock2.acquire()
#         global  num
#         num+=1
#         mylist.append(num)
#         lock2.release()
#         lock1.release()
#
#     def fun2(self):
#         lock2.acquire()
#         time.sleep(0.5)
#         lock1.acquire()
#         global num
#         num += 1
#         mylist.append(num)
#         lock1.release()
#         lock2.release()
#
#
# t1 = myThread(1)
# t2 = myThread(2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(mylist)

# RLock 重复锁，递归锁，可以锁很多次，但是解锁一一对应
# rlock = threading.RLock()
# rlock.acquire()
# rlock.acquire()
# rlock.acquire()
# rlock.acquire()
#
# rlock.release()
# rlock.release()
# rlock.release()
# rlock.release()

# Condition条件锁
#生产者消费者模式

# 生产者负责生产
# guo = []
#
# condition = threading.Condition()
#
# class Produce(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         condition.acquire()
#         while True:
#             time.sleep(1)
#             guo.append("鱼丸")
#             print("%s生产者,放了一个鱼丸，现在锅内还有%s鱼丸"%(self.name,len(guo)))
#             if len(guo)>=5:
#                 print('锅里已有%s个鱼丸'%len(guo))
#                 condition.notify()
#                 condition.wait()
#
#
#
# # 消费者负责消费
# class Consumer(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         condition.acquire()
#         while True:
#             time.sleep(1.5)
#             guo.pop()
#             print("%s消费者,吃了一个鱼丸，现在锅内还有%s鱼丸" % (self.name, len(guo)))
#             if len(guo)<=0:
#                 print("锅里没有鱼丸了，请添加。。")
#                 condition.notify()
#                 condition.wait()
#
# #
# #
# pro = Produce()
# pro.start()
#
#
# con = Consumer()
# con.start()