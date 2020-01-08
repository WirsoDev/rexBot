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



    def shuffleproxies(self):
        
        proxies = ['185.37.211.222:50330', '95.136.51.249:8080', 
                   '213.58.202.70:54214', '5.206.230.62:59355',
                   '193.136.119.21:80', '88.210.71.234:61357']

        proxy = random.choice(proxies)
        return proxy



    def sithtranslator(self):
        proxy = self.shuffleproxies()
        print(f'Proxy use:{proxy}')
        url = f'https://api.funtranslations.com/translate/sith.json?text={self.text}'
        getpage = requests.get(url, proxies={"http": proxy, "https": proxy})
        return getpage.json()



text = "The force is strong in you!"
api = SithTranslator(text)



print(api.sithtranslator())
