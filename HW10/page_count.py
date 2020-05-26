import re

if __name__ == "__main__":
    file1 = 'pdf1.pdf'
    file2 = 'python.pdf'
    rx_pages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE | re.DOTALL)
    with open(file2, "rb") as f:
        data = f.read()
        count = len(rx_pages.findall(str(data)))
    print(count)