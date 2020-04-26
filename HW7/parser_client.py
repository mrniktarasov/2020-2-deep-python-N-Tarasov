from HW7.HttpRequest import HttpRequest

url = input('Enter url: ').encode('utf-8')
request = HttpRequest(url)
data = request.request()
print(data)