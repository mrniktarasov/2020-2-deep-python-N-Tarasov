import urllib

doc = urllib.urlopen('https://stackoverflow.com/').read()
print(doc[:50])
