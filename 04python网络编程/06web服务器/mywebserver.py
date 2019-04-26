import socketserver




class myReqeustHandler(socketserver.BaseRequestHandler):
    def handle(self):
        header = self.request.recv(1024).decode()
        self.myHeader(header)
        print(self.requestobj)

        self.request.sendall("HTTP/1.1 201 OK\r\n\r\n".encode())
        self.request.sendall("<div>this is box</div>".encode())

    def myHeader(self,header):
        arr = header.split("\r\n")
        self.requestobj = dict()
        if arr[0].startswith("GET"):
            self.requestobj['methods'] = "GET"
        elif arr[0].startswith("POST"):
            self.requestobj['methods'] = "POST"

        arr = [item for item in arr if item!="" and arr.index(item)!=0]
        obj = { k:v for k,v in [ item.split(": ") for item in arr]}
        self.requestobj.update(obj)


    def myResponse(self):
        """
        给浏览器进行响应
        :return:
        """
        pass

server = socketserver.ThreadingTCPServer(("192.168.32.101",8000),myReqeustHandler)
server.serve_forever()