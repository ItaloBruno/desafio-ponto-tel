import html2text
import validators
import asyncio
import aiohttp

# Definição do extrator de dados da pápina HMTL
HTML =  html2text.HTML2Text()
HTML.ignore_links=True

async def set_key_value(url: str, page: str, redis) -> None:
    with await redis.conn as r:
        print('Salvando no banco...')
        await r.set(url, page)    

async def get_key_value(url: str, redis) -> str:
    with await redis.conn as r:
        print('Pegando valor salvo no banco...')
        result = await r.get(url)
        return result

async def get_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text()
            return data

async def count_number_word(url: str, word: str, redis) -> dict:
    print('Iniciando Craler na url {}...'.format(url))
    if not validators.url(url, public=True):
        return {
            'url': url,
            'number_of_repititions': 0,
            'status':False
        }
    page = await get_key_value(url, redis)
    if not page:
        page = await get_html(url)
        await set_key_value(url, page, redis)
    
    page = str(page)
    data_page = HTML.handle(page).lower()
    count = data_page.count(word)
    return {
        'url': url,
        'number_of_repititions': count,
        'status':True
    }

async def crawler(urls: list, word: str, redis) -> list:
    """
        Esta função é responsável por pegar o HTML da URL informada como parâmetro da função
        e contar o número de vezes que uma determinada palavra se repete nesta página web.
    """
    print('Iniciando Crawler...')
    
    word = word.lower()
    results = await asyncio.gather(*(count_number_word(url, word, redis) for url in urls))

    return list(results)
