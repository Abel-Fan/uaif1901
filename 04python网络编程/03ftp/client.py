import socket

ip_port = ("127.0.0.1",8000)

sk = socket.socket()
try:
    sk.connect(ip_port)
except:
    print("服务器连接失败")

while True:
    path = sk.recv(1024).decode()
    commend = input("%s>"%path)
    arr = commend.split()
    commend = " ".join(arr)

    sk.send(commend.encode())
    res = sk.recv(1024).decode()
    print(res)