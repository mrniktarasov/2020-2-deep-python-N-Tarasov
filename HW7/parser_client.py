import socket


url = input('Enter url: ')
sock = socket.socket()
sock.connect(('127.0.0.1', 10001))
sock.sendall(url.encode('utf-16'))
data = sock.recv(1024)
sock.close()
print(data.decode('utf-16'))
