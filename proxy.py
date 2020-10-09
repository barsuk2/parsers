
import requests
from bs4 import BeautifulSoup as bs
import parsing.for_pars as pars
from os import path
from time import sleep
from random import randint

URL = 'http://nikulux.ru'
# QUERY = 'промышленные%20пылесосы'
# QUERY = 'пылесосы'
PAGE_PART ='&p='
# folder_for_saving_html = 'hold_searche_yandex_html'
proxies = {'http': '89.184.1.231:3131'}
html1 = requests.get(url=URL, proxies=proxies)
print(html1.status_code)

