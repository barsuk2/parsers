import requests
from bs4 import BeautifulSoup as bs


url = 'https://yandex.ru/search/?text='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.198','Accept': '*/*'}
query = 'купить%20окна'
page_part ='&p='


def get_html(url,params=None):
    r = requests.get(url, headers=headers, params= params)
    return r


def parse():
    html = get_html(url)
    # Integer Code of responded HTTP Status, e.g. 404 or 200.
    if html.status_code == 200:
        get_content(html)
        # print(html.text) # content of the response

    else:
        print('Произошла ошибка')
def get_content(html):
    soup = bs(html,'html.parser')
    items = soup.find_all('a' , class_="dark_link option-font-bold font_sm")
    print(items)
parse()