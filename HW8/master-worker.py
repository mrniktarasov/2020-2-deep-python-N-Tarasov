import urllib.request
from bs4 import BeautifulSoup
import string
import jsonpickle
import socket
from HW8.config import threadsNum
import threading
from queue import Queue
from socket import error as SocketError
import errno


class Parser(threading.Thread):
    def __init__(self, queue, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock

    def run(self):
        while True:
            obj = self.queue.get()
            counter = obj['counter']
            url = obj['url']
            conn = obj['conn']
            text = self.get_text_from_site(url)
            json = text.encode('utf-8')
            self.lock.acquire()
            counter += 1
            conn.sendall(json)
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


def run_server(host, port):
    lock = threading.Lock()
    queue = Queue()
    counter = 0
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen()
        for i in range(threadsNum):
            t = Parser(queue, lock)
            t.setDaemon(True)
            t.start()
        while True:
            conn, addr = sock.accept()
            conn.settimeout(30)
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
                url = jsonpickle.decode(data)
                obj = {
                    'conn': conn,
                    'url': url,
                    'counter': counter,
                }
                queue.put(obj)
        queue.join()
        conn.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10001
    run_server(host, port)
