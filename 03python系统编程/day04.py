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
from multiprocessing import Process,Queue,Pipe
import queue,time

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