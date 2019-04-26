import socketserver,re




class myReqeustHandler(socketserver.BaseRequestHandler):
    def handle(self):
        header = self.request.recv(1024).decode()
        self.myHeader(header)
        self.route()

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

    def route(self):
        """
        根据url地址执行不同的业务逻辑
        :return:
        """
        if "Referer" in self.requestobj:
            referer = self.requestobj['Referer']
            print(referer)
            dirurl = re.search(r"(http|https)://.*?/(.*)",referer).group(2)


        # url = re.search(r"http[s]?://.*?/(.*)",refere)
        # print(url)
        self.myResponse()


    def myResponse(self):
        """
        给浏览器进行响应
        :return:
        """
        self.request.sendall("HTTP/1.1 201 OK\r\n\r\n".encode())
        self.request.sendall("<div>this is box</div>".encode())

server = socketserver.ThreadingTCPServer(("192.168.32.101",8000),myReqeustHandler)
server.serve_forever()