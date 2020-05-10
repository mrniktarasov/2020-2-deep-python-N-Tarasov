import socket
import jsonpickle


urls = 'https://www.codewars.com/'
host = '127.0.0.1'
port = 10001
data = jsonpickle.encode(urls).encode('utf-8')
sock = socket.socket()
sock.connect((host, port))
sock.sendall(data)
sock.settimeout(5)
while True:
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