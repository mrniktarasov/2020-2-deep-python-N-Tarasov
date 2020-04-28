class HttpResponse:
    def __init__(self, words):
        top_words = {
            'top_10_words': {},
        }
        for key, value in words.items():
            top_words['top_10_words'][key] = value
        self.top_ten_words = top_words

