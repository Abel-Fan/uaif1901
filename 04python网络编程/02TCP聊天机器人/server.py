import socket
import requests,json

ip_port = ("127.0.0.1",8000)

sk = socket.socket()
sk.bind(ip_port)
print("开始监听")
sk.listen(5)
print("accept")

yuju = {
    'hello':"hi"
}


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


conn,addr = sk.accept()
while True:
    data = conn.recv(1024).decode()
    text = getInfo(data)
    conn.send(text.encode())
