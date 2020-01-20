# test webscrapping metalinjection
# Handling return/output! 

import requests
from bs4 import BeautifulSoup as bs
import lxml
import itertools


class Metalinj:
    def __init__(self):
        self.url = url = 'https://metalinjection.net/category/upcoming-releases/heavy-new-releases'




    def newspagelink(self):
        '''Extract the news page'''

        page = requests.get(self.url).text
        bspage = bs(page, 'html.parser')

        newspage = bspage.find('h2', class_='title')

        return newspage.a['href']

    
    def getnewshtml(self):
        '''get full html news page'''


        link = self.newspagelink()
        page = requests.get(link).text
        bspage = bs(page, 'html.parser')

        article_detail = bspage.find('div', class_='article-detail thearticlecontent')

        return article_detail

    
    def bandsname(self):
        '''Extract all bands names from page - returns a list'''

        bandsnamelist = []

        for bands in self.getnewshtml().findAll('h3'):
            bands = bands.text
            if bands != 'Subscribe To Our Daily\xa0Dose\xa0Newsletter':
                bands = str(bands.replace('\xa0', ''))
                bandsnamelist.append(bands)

        return bandsnamelist


    def imagelink(self):

        imagelinklist = []

        for images in self.getnewshtml().findAll('h3'):
            extract = images.img
            try:
                imagelinklist.append(extract.get('src'))
            except AttributeError:
                pass

        return imagelinklist



    def description(self):

        descriptionlist = []

        for details in self.getnewshtml().findAll('p'):
            details = details.text
            descriptionlist.append(details)

        del descriptionlist[0:3]
        
        return descriptionlist


        
if __name__ == "__main__":
    bands = Metalinj()
    
    count = len(bands.bandsname()) - 1
    index = 0
    index_2 = 0
    while count >= 0:
        try:
            print('')
            print(bands.bandsname()[index])
            print(bands.imagelink()[index])
            print(bands.description()[index_2])
            print(bands.description()[index_2 + 1])
            index += 1
            index_2 *= 3
        except IndexError:
            pass


    
        