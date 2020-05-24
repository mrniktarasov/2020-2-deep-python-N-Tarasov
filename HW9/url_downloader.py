import asyncio
import aiohttp
from sys import argv
from parse_url import get_text_from_site


async def fetch(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        text = get_text_from_site(data)
        print(f"{url} downloaded \n")


async def main(connections_num, file_with_urls):
    tasks = list()
    conn = aiohttp.TCPConnector(limit = connections_num)

    async with aiohttp.ClientSession(connector=conn) as session:
        with open(file_with_urls, 'r') as file:
            for line in file:
                newLine = line.rstrip()
                tasks.append(asyncio.create_task(fetch(newLine, session)))

            await asyncio.gather(*tasks)


if __name__ == '__main__':
    connections_num = int(argv[1])
    file_with_urls = argv[2]
    #connections_num = 10
    #file_with_urls = 'urls.txt'
    asyncio.run(main(connections_num, file_with_urls))