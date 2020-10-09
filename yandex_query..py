import requests
from bs4 import BeautifulSoup as bs
import parsing.for_pars as pars
from os import path
from time import sleep
from random import randint
from os import mkdir
import os

URL = 'https://yandex.ru/search/?text='
QUERY = 'промышленные%20пылесосы'
QUERY = 'велосипед%20горный'
PAGE_PART = '&p='
folder = 'bicycle_html'
name_files = 'bicycle_ya'
deep = 1
proxy = {'http': '89.184.1.231:3130'}
proxy = None

pars.search_query_yandex(
    deep=5,
    URL=URL,
    QUERY=QUERY,
    PAGE_PART=PAGE_PART,
    folder= folder,
    name_files=name_files,
    # timer_=5
                         )


