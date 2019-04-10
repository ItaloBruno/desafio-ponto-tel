import requests
import html2text

url = 'https://github.com/ItaloBruno'
key_word = 'docker'
page = requests.get(url)

print(page)

h = html2text.HTML2Text()
h.ignore_links=True

data = h.handle(page.text)

data = data.lower()

count = data.count(key_word)

print(data)
print('Quantidade de vezes que a palavra "{}" se repetiu na url "{}": {}'.format(key_word, url, count))