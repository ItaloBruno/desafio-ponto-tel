import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

print(f"started at {time.strftime('%X')}")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(f"finished at {time.strftime('%X')}")
