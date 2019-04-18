import html2text
import validators
import asyncio
import aiohttp

HTML =  html2text.HTML2Text()
HTML.ignore_links=True

async def get_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text()
            return data

async def count_number_word(url: str, word: str) -> dict:
    if not validators.url(url, public=True):
        return {
            'number_of_repititions': 0,
            'status':False
        }
    page = await get_html(url)
    data_page = HTML.handle(page).lower()
    count = data_page.count(word)
    return {
        'number_of_repititions': count,
        'status':True
    }

async def crawler(urls: list, word: str) -> dict:
    """
        Esta função é responsável por pegar o HTML da URL informada como parâmetro da função
        e contar o número de vezes que uma determinada palavra se repete nesta página web.
    """
    print('Iniciando Crawler...')
    
    word = word.lower()
    results = await asyncio.gather(*(count_number_word(url, word) for url in urls))

    return dict(zip(urls, results))
