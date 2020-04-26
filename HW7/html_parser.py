import urllib.request
from bs4 import BeautifulSoup
import string
from collections import OrderedDict
import socket
from HW7.HttpResponse import HttpResponse


def get_text_from_site(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk).lower()
    mask = string.ascii_lowercase + ' ' + ''
    for ch in text:
        if ch not in mask:
            text = text.replace(ch, ' ')
    return text


def make_unnecessary_words_dict():
    return {
            '':     True,
            'a':    True,
            'an':   True,
            'the':  True,
            'in':   True,
            'at':   True,
            'to':   True,
            'on':   True,
            'for':  True,
            'of':   True,
            'by':   True,
    }


def count_words(text):
    art = make_unnecessary_words_dict()
    words = dict()
    text_arr = text.split(' ')
    for word in text_arr:
        if not art.get(word):
            if words.get(word):
                words[word] += 1
            else:
                words[word] = 1
    return words


def top_ten_words(url):
    text = get_text_from_site(url)
    words = count_words(text)
    top = sorted(words.values(), reverse=True)[:10]
    result = OrderedDict()
    for max_value in top:
        for key, value in words.items():
            if value == max_value:
                result[key] = max_value
                break
    return result


def http_handler(func):
    def wrapper(*args, **kwargs):
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 10001))
            sock.listen()
            conn, addr = sock.accept()
            conn.settimeout(10)
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                    except socket.timeout:
                        print('Close connection by timeout')
                        break
                    if not data:
                        break
                    response = func(data)
                    conn.send(response.json)
        return wrapper


@http_handler
def html_top_ten_words(request):
    result = top_ten_words(request.url)
    return HttpResponse(result)

