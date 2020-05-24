import urllib.request
from bs4 import BeautifulSoup
import string
import socket
from HW8.config import threadsNum
import threading
from queue import Queue
from socket import error as SocketError
import errno
import signal
import os
import daemon as dm


class Parser(threading.Thread):
    def __init__(self, queue, lock, i):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.name = 'Thread N{}'.format(i + 1)

    def run(self):
        while True:
            obj = self.queue.get()
            url = obj['url']
            conn = obj['conn']
            text = self.get_text_from_site(url)
            response = text.encode('utf-8')
            test_answer = '{} downloaded with {}; '.format(url, self.name).encode('utf-8')
            self.lock.acquire()
            global counter
            counter += 1
            try:
                conn.sendall(test_answer)
            except BrokenPipeError:
                print('Client is no longer recieves messages')
            self.lock.release()

    def get_text_from_site(self, url):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        # удаление скриптов и стилей
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()

        # убирает начальные и конечные пробелы в каждой
        lines = (line.strip() for line in text.splitlines())
        # разбиение заголовков
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # удалить пустые строки
        text = '\n'.join(chunk for chunk in chunks if chunk).lower()
        mask = string.ascii_lowercase + ' ' + ''
        for ch in text:
            if ch not in mask:
                text = text.replace(ch, ' ')
        return text


def run_server(host='127.0.0.1', port=10001):
    lock = threading.Lock()
    queue = Queue()
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen()
        for i in range(threadsNum):
            t = Parser(queue, lock, i)
            t.setDaemon(True)
            t.start()
        conn, addr = sock.accept()
        conn.settimeout(10)
        while True:
            try:
                data = conn.recv(1024)
            except socket.timeout:
                print('Close connection by timeout')
                break
            except SocketError as e:
                if e.errno != errno.ECONNRESET:
                    raise  # Not error we are looking for
                pass  # Handle error here.
            if data:
                url = data.decode('utf-8')
                obj = {
                    'conn': conn,
                    'url': url,
                }
                queue.put(obj)
        queue.join()
        conn.close()


def exit(signalNumber, frame):
    global counter
    print('Received:', signalNumber)
    print('Total urls downloaded: {}'.format(counter))
    raise SystemExit('Exiting')
    return


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10001
    counter = 0
    signal.signal(signal.SIGUSR1, exit)
    print('My PID is:', os.getpid())
    #with dm.DaemonContext():
    run_server(host, port)


#sudo netstat -tulpn | grep LISTEN