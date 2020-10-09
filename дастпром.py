import requests
import parsing.for_pars as ps
from bs4 import BeautifulSoup as bs

url = 'https://www.prompylesos.ru/catalog/pylesosy-dastprom/dvukhfaznye-pylesosy/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.198','Accept': '*/*'}

folder_for_saving_html = 'hold_searche_yandex_html'
html = requests.get(url, headers)
ps.write_to_file_html('dastprom.html',html.text)
html = ps.read_file_html('dastprom.html')
# print(html)
soup = bs(html,'html.parser')
l =soup.find_all(class_="dark_link option-font-bold font_sm")
for  i in l:
    print(i.get_text())
# ps.write_to_f
#
