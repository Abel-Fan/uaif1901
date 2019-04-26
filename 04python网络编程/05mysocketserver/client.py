import socket

ip_port = ("127.0.0.1",8000)
sk = socket.socket()
try:
    sk.connect(ip_port)
except:
    print("服务器无法连接")

sk.send('hello world'.encode())