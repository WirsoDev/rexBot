import requests as rq
from bs4 import BeautifulSoup as bs


def get_last_url():
    # return a ulr for the last entry

    url = 'https://progreport.com/category/latest-progressive-rock-news/'
    conn = rq.get(url)

    status = conn.status_code

    if status == 200:
        soup = bs(conn.text, 'html.parser')
        mydivs = soup.find_all("h2", {"class": "entry-title h3"})
        last_url = mydivs[0].a['href']
        return(last_url)
    else:
        return False
    

def prog_controller():
    with open(r'external_api/logs/prognews_controller.txt', 'r') as txt:
        return txt.read().strip() == get_last_url()

