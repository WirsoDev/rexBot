import requests
from bs4 import BeautifulSoup as bs
import json
import string

url = 'http://spys.one/free-proxy-list/PT/'

page = requests.get(url).text
bspage = bs(page, 'html.parser')


# print(bspage.find('font', class_='spy14'))

for x in bspage.find_all('font', class_='spy14'):
    print(x.text)







