# test webscrapping metalinjection
# Handling return/output! 

import requests
from bs4 import BeautifulSoup as bs
import lxml


class Metalinj:
    def __init__(self, url):
        self.url = url


    def handshake(self):

        '''Simple handshake test'''

        page = requests.get(self.url)
        return page



    def newspagelink(self):
        '''Extract the news page'''

        page = requests.get(self.url).text
        bspage = bs(page, 'html.parser')

        newspage = bspage.find('h2', class_='title')

        return newspage.a['href']

    
    def getnewshtml(self):
        '''get full html news page - extract data'''


        link = self.newspagelink()
        page = requests.get(link).text
        bspage = bs(page, 'html.parser')

        image = []
        band_album = []
        description = []
        description_2 = []

        article_detail = bspage.find('div', class_='article-detail thearticlecontent')

        # extract band + album name

        for names in article_detail.findAll('h3'):
            files = names.text
            if files != 'Subscribe To Our Daily\xa0Dose\xa0Newsletter':
                files = str(files.replace('\xa0', ''))
                band_album.append(files)

        # extract image.url
        
        for images in article_detail.findAll('h3'):
            extract = images.img
            try:
                image.append(extract.get('src'))
            except AttributeError:
                pass

        # extract details | 3 itens by title

        for detail in article_detail.findAll('p'):
            details = detail.text
            description.append(details)
        
        del description[0:3]

        count =len(band_album)
        index = 0
        while count >= 0:
            for x in range(3):
                description_2.append(description[index])
                index += 1
            count -= 1

        