import requests
import html2text
import validators
import asyncio
import time

async def crawler(url, key_word):
    """
        Esta função é responsável por pegar o HTML da URL informada como parâmetro da função
        e contar o número de vezes que uma determinada palavra se repete nesta página web.
    """

    # Estrutura do retorno desta função
    result = {
        'url': url,
        'number_of_repititions': 0,
        'status': False
    }
    
    key_word = key_word.lower()

    if not validators.url(url, public=True):
        return result

    page = requests.get(url)

    if page.status_code == 200:
        html = html2text.HTML2Text()
        html.ignore_links=True

        data_page = html.handle(page.text).lower()
        data_page = data_page.lower()
        number_of_repititions = data_page.count(key_word)

        result['number_of_repititions'] = number_of_repititions
        result['status'] = True
    
    return result

async def main():
    await asyncio.gather(
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Sanic'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Maria'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
        crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python'),
    )

print(f"started at {time.strftime('%X')}")
asyncio.run(main())
print(f"finished at {time.strftime('%X')}")

# loop = asyncio.get_event_loop()
# tasks = [
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Sanic')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Maria')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
#     loop.create_task(crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Python')),
# ]
# wait_tasks = asyncio.wait(tasks)

# print(f"started at {time.strftime('%X')}")
# loop.run_until_complete(wait_tasks)
# loop,.get
# print(f"finished at {time.strftime('%X')}")
# loop.close()
