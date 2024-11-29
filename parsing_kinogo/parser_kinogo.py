import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://kinogo.ec'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all('div', id_='dle-content')
    kinogo_list = []
    for item in items:
        title = item.find('div', class_='shortstory__title').get_text(strip=True)
        image = URL + item.find('div', class_='shortstory__poster').find('img').get('src')