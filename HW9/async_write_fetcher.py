import multiprocessing
import time
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor


def write_file(data):
    name = f'photo_{int(time.time() * 1000)}'
    with open(name, 'wb') as f:
        f.write(data)


async def fetch(url, session, loop):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
        await loop.run_in_executor(pool, write_file, data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    loop = asyncio.get_running_loop()

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch(url, session, loop)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()

    print('TT', t2 - t1)