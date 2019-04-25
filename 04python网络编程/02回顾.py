# jQuery实现了轮播图
# 特性：隐式循环链式调用
# 怎么实现隐式循环，链式调用
"""
class jQuery.ini{
    constructor(obj){
        this.obj = obj
    }
    click(fn){
        for(let i=0;i<this.obj.length;i++){
            this.obj[i].onclick = fn
        }
        return this.obj
    }
    mouse(fun){
        for(let i=0;i<this.obj.length;i++){
            this.obj[i].onmouse = fn
        }
        return this.obj
    }
}


function $(selector){

    nodes = document.querySelectorAll(selector)
    return jQuery.ini(nodes)
}

$(".box").click(function(){

}).mouse()






"""

# ajax

# socket
# TCP UDP ftp
# TCP\UDP区别
"""
TCP基于连接的协议，安全性、可靠性更高，效率不高。
三次握手

UPD基于无连接的协议，效率高，但是安全性、可靠性弱。
"""

"""
1、发送 hello world

server.py
（1）实例化套接字
sk = socket.socket(地址族,协议)
地址族：Ipv4 Ipv6 socket.AF_INET  socket.AF_INET6
协议： TCP socket.SOCK_STREAM   UDP socket.SOCK_DGRAM

（2）绑定地址
sk.bind(("127.0.0.1",8000))
（3）监听请求
sk.listen(5)
（4）等待处理请求
conn,addr = sk.accept()
conn 连接、 client socket
addr client地址  (ip,port)





"""