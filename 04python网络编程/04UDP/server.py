import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ("127.0.0.1",8000)

sk.bind(ip_port)
con,addr = sk.recvfrom(1024)
# con 接收的内容  addr client地址
print(con.decode())

# UDP  server 创建流程
# 实例化一个socket
# 绑定ip_prot
# socket.recvform(字节长度) 返回一个元组 (con,addr) (内容,client的地址)

# UDP client 创建流程
# 实例化一个socket
# socket.sendto(data,addr) data发送的内容， addr服务器的地址