import json


class HttpResponse:
    def __init__(self, words):
        self.top_ten_words = words

    def to_json(self):
        top_words = {
            'top_10_words': {},
        }
        for key, value in self.top_ten_words.items():
            top_words['top_10_words'][key] = value
        return json.dumps(top_words)
