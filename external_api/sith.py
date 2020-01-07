'''

Tradutor eng - sith

help:
# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/

lista de proxys PT
http://spys.one/free-proxy-list/PT/

criar uma proxy ramdom para cada request

tentar alterar proxies nos requests
max 10 requests

proxies={"http": proxy, "https": proxy}

'''

import requests
import json
from lxml.html import fromstring
import random
from itertools import cycle
import traceback



class SithTranslator:
    

    def __init__(self, text=''):
        self.text = text


    def genproxy(self):

        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)

        proxies = set()

        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                # Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)

        return proxies


    def checkconnection(self):
        # proxies = self.genproxy()
        # proxy_pool = cycle(proxies)
        url = f'https://api.funtranslations.com/translate/sith.json?text={self.text}'

        for x in range(1, 11):
            # proxy = next(proxy_pool)
            proxy = '95.136.51.249:8080'
            print(f'request #{x} -- proxy: myproxie')
            try:
                response = requests.get(url, proxies={"http": proxy, "https": proxy})
                print(response.status_code)
            except:
                print('Connection error')


    def sithtranslator(self):
        # proxies_01 = '162.144.220.192:80'
        # proxies_01 = self.genproxy()
        url = f'https://api.funtranslations.com/translate/sith.json?text={self.text}'
        getpage = requests.get(url)
        return getpage.json()



text = "The force is strong in you!"
api = SithTranslator(text)



print(api.checkconnection())
