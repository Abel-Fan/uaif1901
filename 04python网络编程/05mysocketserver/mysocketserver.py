import socketserver

# socketserver.ThreadingTCPServer()

class MySocketRquestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        con = self.request.recv(1024)
        print(con.decode(),self.client_address)

server = socketserver.ThreadingTCPServer(('192.168.32.101',8000),MySocketRquestHandler)
server.serve_forever()