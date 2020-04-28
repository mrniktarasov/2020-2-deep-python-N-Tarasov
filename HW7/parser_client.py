import socket
import jsonpickle
from HW7.HttpRequest import HttpRequest


url = input('Enter url: ')
host = '127.0.0.1'
port = 10001
request = HttpRequest(url, host, port)
data = jsonpickle.encode(request).encode('utf-8')
sock = socket.socket()
sock.connect((host, port))
sock.sendall(data)
data = sock.recv(1024)
sock.close()
print(jsonpickle.decode(data).top_ten_words)
