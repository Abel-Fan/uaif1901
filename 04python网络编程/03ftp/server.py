import socket,threading
import os,os.path,random

root = r"C:\Users\yangd\Desktop\uaif1901"

users = {
    'ydh':{
        'password':'123456',
        'home':r"C:\Users\yangd\Desktop\uaif1901\04python网络编程\03ftp"
    },
    'xm':{
        'password':'123456',
        'home':r"C:\Users\yangd\Desktop\uaif1901\04python网络编程\03ftp"
    },
}




def main(conn,addr):
    isLogin = False
    while True:
        # 检测登录
        while not isLogin:
            info = conn.recv(1024).decode()
            username,password = info.split()
            if username in users:

                if users[username]['password']==password:
                    text = "ok %s"%(random.randint(1000,9999))
                    conn.send(text.encode())
                else:
                    conn.send("no 密码错误".encode())
            else:
                conn.send("no 没有此用户".encode())
        # 执行命令







ip_port = ("127.0.0.1",8000)

sk = socket.socket()
sk.bind(ip_port)

sk.listen(5)


while True:
    conn,addr = sk.accept()
    t = threading.Thread(target=main,args=(conn,addr))
    t.start()
