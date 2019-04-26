import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ("192.168.32.255",8000)
sk.sendto("hello world".encode(),ip_port)