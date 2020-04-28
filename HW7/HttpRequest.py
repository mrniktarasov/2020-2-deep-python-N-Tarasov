import json


class HttpRequest:
    def __init__(self, url, host='127.0.0.1', port=10001):
        self.domain = host
        self.port = port
        self.url = url
