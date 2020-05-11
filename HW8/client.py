import socket
import time


urls = ['https://www.python.org/',
        'https://stackoverflow.com/',
        'https://www.codewars.com/']
host = '127.0.0.1'
port = 10001
sock = socket.socket()
sock.connect((host, port))
sock.settimeout(30)
while True:
    for url in urls:
        data = url.encode('utf-8')
        sock.sendall(data)
        time.sleep(2)
    try:
        data_back = sock.recv(2*1024)
    except socket.timeout:
        print('Close connection by timeout')
        break
    decoded = data_back.decode('utf-8')
    print(decoded)
    if not data_back:
        break
sock.close()
