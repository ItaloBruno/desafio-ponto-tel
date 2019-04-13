import requests
import html2text
import validators

def crawler(url, key_word):
    """
        Esta função é responsável por pegar o HTML da URL informada como parâmetro da função
        e contar o número de vezes que uma determinada palavra se repete nesta página web.
    """

    # Estrutura do retorno desta função
    result = {
        'url': url,
        'key-word': key_word,
        'count': 0,
        'status': False
    }
    
    key_word = key_word.lower()

    if not validators.url(url, public=True):
        # print(result)
        return result

    page = requests.get(url)

    if page.status_code == 200:
        html = html2text.HTML2Text()
        html.ignore_links=True

        data_page = html.handle(page.text).lower()
        data_page = data_page.lower()
        count = data_page.count(key_word)

        result['count'] = count
        result['status'] = True
    
    # print(result)
    return result

crawler('https://github.com/huge-success/sanic/blob/master/docs/sanic/getting_started.md', 'Sanic')