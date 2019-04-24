import socket

sk = socket.socket()

try:
    sk.connect(("127.0.0.1",8000))
except:
    print("连接服务器失败")

while True:
    data = input(">").encode()
    sk.send(data)
    res = sk.recv(1024).decode()
    print("服务器:%s"%res)