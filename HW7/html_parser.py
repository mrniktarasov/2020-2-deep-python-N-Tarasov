import urllib.request
from bs4 import BeautifulSoup
import string
import pickle
from collections import OrderedDict
import socket
from HW7.HttpResponse import HttpResponse
from HW7.english_pretexts import english_pretexts


def get_text_from_site(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    # удаление скриптов и стилей
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    # убрает начальные и конечные пробелы в каждой
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


def count_words(text):
    words = dict()
    text_arr = text.split(' ')
    for word in text_arr:
        if not english_pretexts.get(word):
            if words.get(word):
                words[word] += 1
            else:
                words[word] = 1
    return words


def top_ten_words(url):
    text = get_text_from_site(url)
    words = count_words(text)
    top = sorted(words.values(), reverse=True)[0:10]
    result = OrderedDict()
    for max_value in top:
        for key, value in words.items():
            if value == max_value and not result.get(key):
                result[key] = value
                break
    return result


def make_response(request):
    result = top_ten_words(request.url)
    return HttpResponse(result)


def run_server(host, port):
    with socket.socket() as sock:
            sock.bind((host, port))
            sock.listen()
            conn, addr = sock.accept()
            conn.settimeout(5)
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                    except socket.timeout:
                        print('Close connection by timeout')
                        break
                    if not data:
                        break
                    request = pickle.loads(data)
                    response = make_response(request)
                    conn.send(response.to_json().encode('utf-8'))
                conn.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10001
    run_server(host, port)
