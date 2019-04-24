import socket
import requests,json
import threading

ip_port = ("192.168.32.101",8000)

sk = socket.socket()
sk.bind(ip_port)
print("开始监听")
sk.listen(5)
print("accept")

yuju = {
    'hello':"hi"
}

def main(conn):
    while True:
        data = conn.recv(1024).decode()
        text = getInfo(data)
        conn.send(text.encode())


def getInfo(text):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": "%s"%text
            }
        },
        "userInfo": {
            "apiKey": "26572efa06f84ae7a6443e94854de853",
            "userId": "3a21c12aad537feb"
        }
    }
    data = json.dumps(data)
    res = requests.post(url=url,data=data,headers={
        'content-type':'application/json'
    })
    res = json.loads(res.text)
    res2 = res['results'][0]['values']['text']
    return res2
index = 0
while True:
    conn,addr = sk.accept()
    index+=1
    print(index)
    t = threading.Thread(target=main,args=(conn,))
    t.start()

