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
                    text = "ok %s %s"%(random.randint(1000,9999),users[username]['home'])
                    conn.send(text.encode())
                    os.chdir(users[username]['home'])
                    break
                else:
                    conn.send("no 密码错误".encode())
            else:
                conn.send("no 没有此用户".encode())
        # 执行命令
        while True:
            commend = conn.recv(1024).decode()
            arr = commend.split()
            if arr[0] in "ls dir list":
                dirs = os.listdir(os.getcwd())
                text = "\n".join(dirs)
                conn.send(text.encode())
            if arr[0]=='cd':
                if os.path.isdir(arr[1]):
                    os.chdir(os.getcwd()+"\\"+arr[1])
                    text = os.getcwd()
                    conn.send(text.encode())
                elif arr[1] == "..":
                    os.chdir("\\".join( os.getcwd().split("\\").pop() ))
                    text = os.getcwd()
                    conn.send(text.encode())
            if arr[0]=="get":
                if os.path.isfile(arr[1]) and len(arr)>1:
                    text = "ok " + str(os.path.getsize(arr[1]))
                    conn.send(text.encode())
                    with open(arr[1],"rb") as f:
                        con = f.read()
                    conn.send(con)

                else:
                    conn.send("no 没有此文件")








ip_port = ("192.168.32.101",8000)

sk = socket.socket()
sk.bind(ip_port)

sk.listen(5)


while True:
    conn,addr = sk.accept()
    t = threading.Thread(target=main,args=(conn,addr))
    t.start()
