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
import time
arr = []
def Produce(gobj,name):
    gobj.send(None)
    for i in range(1,101):
        time.sleep(1)
        arr.append(i)
        print("%s放了第%s个鱼丸，锅里还有%s个鱼丸"%(name,i,len(arr)))
        if len(arr)>=5:
            gobj.send(i)
# 生成器
def Consumer(name):
    while True:
        i = yield
        time.sleep(1)
        arr.pop()
        print("%s吃了第%s个鱼丸，锅内还剩%s个鱼丸"%(name,i,len(arr)))

gobj = Consumer("小红")
Produce(gobj,"小白")