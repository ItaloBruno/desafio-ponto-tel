import requests
import html2text
import validators
import asyncio
import time


def get_html_data(url: str) -> str:
    page = requests.get(url)
    html = html2text.HTML2Text()
    html.ignore_links=True
    data_page = html.handle(page.text).lower()
    return data_page

def count_number_word(url: str, word: str) -> int:
    data_page = get_html_data(url)
    count = data_page.count(word)
    return count


def crawler(url: str, word: str) -> dict:
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
    
    word = word.lower()

    if not validators.url(url, public=True):
        return result

    result['number_of_repititions'] = count_number_word(url, word)
    result['status'] = True
    
    return result
