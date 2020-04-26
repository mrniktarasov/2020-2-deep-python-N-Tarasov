import socket


class HttpRequest:
    def __init__(self, url, domain='127.0.0.1', port=10001):
        self.domain = domain
        self.port = port
        self.url = url

    def request(self):
        sock = socket.socket()
        sock.connect((self.domain, self.port))
        sock.sendall(self)
        data = sock.recv(1024)
        sock.close()
        return data
