from bs4 import BeautifulSoup as bs
import requests
import lxml

class Randomnames:

    def __init__(self, url):
        self.url = url


    def handshake(self):
        connection = requests.get(self.url)
        print(connection)
        return connection


    def getnames(self):
        conn = requests.get(self.url).text
        page = bs(conn, 'lxml')
        names = page.find('h1')
        print(names)
        
        


if __name__ == "__main__":
    url = 'http://listofrandomnames.com/index.cfm?generated'

    conn = Randomnames(url)
    conn.getnames()