import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm'
page = requests.get(url)
print(page.text)

# soup = BeautifulSoup(page.text, 'html.parser')

# artist_name_list = soup.find(class_='BodyText')

# artist_name_list_items = artist_name_list.find_all('a')

# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())