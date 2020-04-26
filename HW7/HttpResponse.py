import json


class HttpResponse:
    def __init__(self, words):
        top_words = {
            'top_10_words': {},
        }
        for key, value in words.items():
            top_words['top_10_words'][key] = value
        self.json = json.dumps(top_words)
