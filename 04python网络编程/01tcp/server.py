import socket

# 实例化socket对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 参数一
# socket.AF_INET Ipv4
# socket.AF_INET Ipv6
# 参数二
# socket.SOCK_STREAM  TCP协议 (面向连接) 特点：效率要求不是很高，但是安全可靠性要求高时，例如：打电话，收发文件
# socket.SOCK_DGRAM   UDP协议 (面向无连接) 特点：对效率要求高，对内容要求不好时，例如：直播，语音。
ip_port = ("127.0.0.1",8000)  # 元组
sk.bind(ip_port)
print("开始监听.....")
sk.listen(5)  # 监听请求
print("accept...")
conn,addr = sk.accept()   # 响应请求,返回 (conn,addr)  (连接,地址)
print("接收内容...")
data = conn.recv(1024).decode()  # 接收内容
print(data)
sk.close()
