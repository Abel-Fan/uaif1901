# 回顾
# 进程定义
# 进程是正在执行的程序或软件，是系统分配资源最小单元。
# 是执行中的文件以及使用资源（内存虚拟地址，对象句柄，代码，数据，环境变量，执行单元）的总和。
# 线程是系统调度的最小单元。同一进程中的线程之间数据共享的。
# 优势：
# 进程优势：适合做计算密集型任务。计算密集型任务，对图片、视频的处理，计算圆周率。
# 线程优势：适合做IO密集型任务（输入输出：磁盘存储，网络请求）
# 案例: 多线程的拷贝复制
#       （1）myCopy.py  主动修改内部的变量。
#       （2）py文件可以转换为exe文件 可以跟参数  mycopy 文件名，python3.5

# GIL
# 历史原因：硬件
#
"""
from multiprocessing Process
定义的方式类似于线程：
（1）构造函数
（2）继承Process类
注意：创建进程的时需要放 if __name__ == "__main__": 之后

上下文或进程启动方法：
spawn window默认
fork  os.fork() unix系统
forkserver 创建进程的服务器

multiprocessing 常用函数
cpu_count()
active_children()
current_process()
get_all_start_methods()
get_context()
get_start_method()


进程对象方法
pid
run()
start()
name
join()
is_alive()
daemon
authkey()
exitcode
terminate() 立刻终止进程运行
kill()
close()

数据交换
Queue 类似于queue.Queue
"""
from multiprocessing import Process,Queue,Pipe,Array,Value,Pool
from threading import Thread
import threading
import queue,time,random

# def fun1(q):
#     print('fun1 id:', id(que))
#     print(q.get())
#
# def fun2(q):
#     print('fun2 id:', id(que))
#     time.sleep(2)
#     q.put(123)
#
#
# que = Queue(5)
# que2 = queue.Queue(5)
#
# if __name__ == "__main__":
#     print('id:',id(que2))
#     p1 = Process(target=fun1,args=(que2,))
#     p1.start()
#     p2 = Process(target=fun2,args=(que2,))
#     p2.start()

#
# def fun1(con1):
#     con = con1.recv()
#     con1.send("this is fun1")
#     print(con)
#
# def fun2(con2):
#     con = con2.recv()
#     print(con)
#     con2.send("this is fun2")
#
# con1,con2 = Pipe()  # 实例化时会返回两个对象，管道两个端口
#
# if __name__ == "__main__":
#     p1 = Process(target=fun1,args=(con1,))
#     p1.start()
#     p2 = Process(target=fun2,args=(con2,))
#     p2.start()

# 一个进程 既能接收信息也能发送信息

# def tfun1(pi,name):
#     while True:
#         print("%s接收消息：%s"%(name,pi.recv()))
# def tfun2(pi,name):
#     while True:
#         time.sleep(random.randint(1,5))
#         con = name+":"+str(time.time())
#         print("%s发送了消息"%name)
#         pi.send(con)
#
# def fun1(pi):
#     # 发送消息
#     t2 = Thread(target=tfun2, args=(pi, 'process-1'))
#     t2.start()
#     # 接收消息
#     t1 = Thread(target=tfun1,args=(pi,"process-2"))
#     t1.start()
#     print("p1",threading.enumerate())
#
# def fun2(pi):
#     # 向进程p1发送消息
#     t2 = Thread(target=tfun2, args=(pi, 'process-2'))
#     t2.start()
#     # 接收
#     t1 = Thread(target=tfun1, args=(pi,'process-1'))
#     t1.start()
#
#
#
# if __name__ == "__main__":
#     con1,con2 = Pipe()
#     p1 = Process(target=fun1,args=(con1,))
#     p2 = Process(target=fun2,args=(con2,))
#     p1.start()
#     p2.start()

# def fun1(arr,value):
#     arr[0] = 9
#     for i in range(len(arr)):
#         arr[i]=arr[i]+1
#
#     value.value = 10
# def fun2(arr,value):
#     time.sleep(2)
#     for i in arr:
#         print(i)
#     print(value.value)
#
#
#
# if __name__ == "__main__":
#
#     arr = Array('b',range(10)) #  Array('模式','数据')
#     value = Value('b',1)
#     p1 = Process(target=fun1,args=(arr,value))
#     p1.start()
#
#     p2 = Process(target=fun2, args=(arr,value))
#     p2.start()

# 进程池 Pool
# def fun():
#     time.sleep(1)
#     return 123
#
# def fun2(item):
#     return item+1
#
# if __name__ == "__main__":
#     pool = Pool(100)  # 创建进程池 5代表进程池的进程数量
#     # res =pool.apply(fun)
#     # res = pool.apply_async(fun)
#     # res.wait()
#     # print(res.get())
#     start = time.time()
#     res = pool.map(fun2,range(100000))
#     # res = map(fun2,range(100000))
#     for i in res:
#         print(i)
#     print(res)
#     end = time.time()
#     print('运行总时间：%s'%(end-start))


# if __name__ == '__main__':
    # start = time.time()
    # x = [list(range(10)), list(range(20,30)),
    #      list(range(50,60)), list(range(80,90))]
    # with Pool(2) as p:
    #     print(p.map(sum, x))

    # print(list(map(sum,x)))

    # end = time.time()
    #
    # print("运行总时间%s"%(end-start))


# 进程池
# 为什么要用进程池：
# pool = Pool(num)
# apply(fun,args=(),kwds={})
# 通过进程池对象调用fun函数,阻塞主进程运行
# apply_async(fun,args=(),kwds={},callback=函数,error_callback=函数)
# 通过进程池对象调用fun函数，不会阻塞主进程，callback 进程成功执行完成的回调函数。error_callback 进程执行失败执行的回调函数
# map(函数,iter)  是 map()函数的多进程版本

# def fun(num):
#     time.sleep(2)
#     arr = []
#     for i in range(num):
#         arr.append(i+1)
#     return arr
#
#
# def fun2(item):
#     print("调用完成。。。。")
#
# def fun3(item):
#     print("error")
if __name__ == "__main__":
    pool = Pool(5)
    arr = list(range(1,10000))
    # apply
    # for i in range(1,21):
    #     res = pool.apply(fun,args=(i,))
    #     print(res)

    # apply_async()
    #
    # for i in range(1,21):
    #     applyObje = pool.apply_async(fun,args=(i,),callback=fun2,error_callback=fun3)
    #     arr.append(applyObje)
    #
    # for item in arr:
    #     item.wait()
    #     print(item.get())
    start = time.time()
    res1 = sum(arr)
    res2 = sum(range(1,20))
    res3 = sum(range(10,40))
    res4 = sum(range(100,300))
    res5 = sum(range(500,1000))
    # res = pool.map(sum,[arr,range(1,20),range(10,40),range(100,300),range(500,1000)])
    # print(res)
    print(res1,res2,res3,res4,res5)
    end = time.time()

    print("end...时间：%s"%(end-start))