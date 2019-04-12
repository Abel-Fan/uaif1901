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
class myThread1(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        # print("myThread1",threading.current_thread())
        for i in range(10):
            time.sleep(1)
            arr.append(i)
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





