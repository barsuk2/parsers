import requests
from bs4 import BeautifulSoup as bs
from os import path
from time import sleep
from random import randint
from os import mkdir
import os

URL = 'https://yandex.ru/search/?text='
QUERY = 'промышленные%20пылесосы'
QUERY = 'велосипед'
PAGE_PART = '&p='
folder = 'bicycle_html'
name_files = 'bicycle_ya'
deep = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.198', 'Accept': '*/*'}

query_yandex = 'промышленные%20пылесосы'
page_part_yandex = '&p=2'


def write_to_file_html(file, html):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)


def read_file_html(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def search_query_yandex(deep: int, name_files: str, folder: str,
                        PAGE_PART, URL: str, QUERY, proxy=None, timer_=120 ):
    if deep <=0 :
        print('Глубина не в диапазоне >=1')
    if folder not in os.listdir(os.curdir):
        os.mkdir(folder)
    flag = True if deep == 1 else False #хотим одно значение
    for i in range(deep):
        if i != 0:
            page_part = f'{PAGE_PART}{str(i)}'
        else:
            page_part = ''

        url = f'{URL}{QUERY}{page_part}'
        print(url)
        html = requests.get(url=url, headers=headers, params=None, proxies=proxy)
        text = html.text
        file = path.join(folder, f'{name_files}_{i}.html')
        write_to_file_html(file, text)
        if flag is True: # Для получения глубины 1 страница
            break
        timer = randint(timer_, timer_+90)
        sleep(timer)
        print(i, timer)


if __name__ == '__main__':
    search_query_yandex(deep=1, URL=URL, QUERY=QUERY,PAGE_PART=PAGE_PART, folder= folder, name_files=name_files)
