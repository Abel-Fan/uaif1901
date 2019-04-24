import socket,threading
import os

def main(conn,addr):
    while True:
        os.chdir(r"C:\Users\yangd\Desktop\uaif1901")
        conn.send(r"C:\Users\yangd\Desktop\uaif1901".encode())
        commend = conn.recv(1024).decode()

        if "dir" in commend:
            arr = os.listdir(os.getcwd())
            res = "\n".join(arr)
            print(res)
            conn.send(res.encode())




ip_port = ("127.0.0.1",8000)

sk = socket.socket()
sk.bind(ip_port)

sk.listen(5)


while True:
    conn,addr = sk.accept()
    t = threading.Thread(target=main,args=(conn,addr))
    t.start()
