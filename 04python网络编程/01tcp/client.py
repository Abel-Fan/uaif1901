import socket
sk = socket.socket()  # 默认就是Ipv4  socket.STREAM

ip_port = ("127.0.0.1",8000)

try:
    # 建立连接
    sk.connect(ip_port)
except:
    print("服务器端未开启...")

sk.send("hello world".encode())
sk.close()