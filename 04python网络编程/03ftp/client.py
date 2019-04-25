import socket
import getpass

ip_port = ("127.0.0.1",8000)

sk = socket.socket()
try:
    sk.connect(ip_port)
except:
    print("服务器连接失败")

num = ""

# 流程不对
"""
客户端登录流程
cookie
查看cookie是否存在
存在 ->跳过登录
不存在 -> 执行登录
登录成功-> 设置cookie 跳过登录
登录失败->执行登录


服务端登录流程
验证用户身份
是->登录成功 发送 cookie
不是->登录失败 发送 登录失败




"""
cookie = "0"

def login():
    username = input("root@%s's username:"%(ip_port[0]))
    password = getpass.getpass("root@%s's password:"%(ip_port[0]))
    con = "%s %s"%(username,password)
    sk.send(con.encode())

while True:
    # 如果cookie==0 登录 不等于0 跳过
    while cookie=="0":
        login()
        res = sk.recv(1024).decode() # 登录结果  "ok cookie"  "no message"
        code,mes = res.split()
        if code == "ok":
            cookie = mes
            print(cookie)
            break
        elif code == "no":
            print(mes)

    print("登录成功")

