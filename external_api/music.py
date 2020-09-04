
import requests
from bs4 import BeautifulSoup as bs
import lxml
import itertools


class Metalinj:
    def __init__(self):
        self.url = 'https://metalinjection.net/category/upcoming-releases/heavy-new-releases'

    def newspagelink(self):
        '''Extract the news page'''

        page = requests.get(self.url).text
        bspage = bs(page, 'html.parser')

        newspage = bspage.find('h2', class_='zox-art-title')

        return newspage.a['href']

    def getnewshtml(self):
        '''get full html news page'''

        link = self.newspagelink()
        page = requests.get(link).text
        bspage = bs(page, 'html.parser')

        article_detail = bspage.find(
            'div', class_='article-detail thearticlecontent')

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

    def youtube(self):

        youtubelist = []

        for links in self.getnewshtml().findAll('iframe'):
            links = links.get('src')
            transformedlinks = str(links.replace('embed/', 'watch?v='))
            youtubelist.append(transformedlinks)

        return youtubelist

    def drooping(self):
        '''Return the other droops in music (also dropping)'''

        droopinglist = []

        for x in self.getnewshtml().findAll('li'):
            droopinglist.append(x.text)

        return droopinglist

    def controller(self):
        file = open(r'external_api/logs/metalinj_rsscontroler.txt', 'r')
        controller = file.read()
        x = self.bandsname()[0]
        return x == controller


if __name__ == "__main__":
    pass
