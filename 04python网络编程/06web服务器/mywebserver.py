import socketserver,re

class Route:
    def __init__(self,request,request_dic):
        self.request = request
        self.request_dic = request_dic
        self.urls = ['/index','/show','/list']
    def route(self):
        if self.request_dic['url'] in self.urls:
            url = self.request_dic['url']
            if url=="/index":
                self.return_render_template("index.html")
            elif url == "/show":
                self.return_render_template("show.html")
            elif url =="/list":
                self.return_render_template("list.html")

        else:
            self.return_404_response()

    def return_render_template(self,filename):
        with open("./templates/%s"%filename,"rb") as f:
            response_text = "HTTP/1.1 200 OK\r\n\r\n".encode()
            content_text = f.read()
            self.request.sendall(response_text)
            self.request.sendall(content_text)


    def return_404_response(self):
        response_text = "HTTP/1.1 200 OK\r\n\r\n".encode()
        content_text = "<html><head><meta charset='UTF-8'></head><body><div>404页面找不到了。。。。</div></body></html>".encode()
        self.request.sendall(response_text)
        self.request.sendall(content_text)


# 请求处理器
class myReqeustHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request_header = self.request.recv(1024).decode()  #请求头
        self.create_request_header(request_header)

        # 路由器（根据虚拟路径，执行不同后台处理程序
        route = Route(self.request,self.request_dic)
        route.route()

    def create_request_header(self,request_header):  #创建请求头对象
        header_info_arr = request_header.split("\r\n")
        method,url,http_v =header_info_arr[0].split()
        self.request_dic = {
            'method':method,
            'url':url,
            'http_v':http_v
        }
        obj = { k:v  for k,v in [ item.split(": ") for item in header_info_arr if header_info_arr.index(item)>0 and item !=""]}
        self.request_dic.update(obj)
        print(self.request_dic)



server = socketserver.ThreadingTCPServer(("192.168.32.101",8000),myReqeustHandler)
server.serve_forever()