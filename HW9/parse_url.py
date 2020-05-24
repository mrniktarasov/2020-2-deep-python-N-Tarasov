from bs4 import BeautifulSoup
import string


def get_text_from_site(html):
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
