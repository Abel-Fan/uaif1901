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
import time
print("主线程开始")
def fun():
    time.sleep(2)
    return True
con.wait_for(fun)   # 阻塞，直到 predicate 返回True
print("主线程结束..")


