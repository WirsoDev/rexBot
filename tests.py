from bs4 import BeautifulSoup as bs
import lxml


conn = bs('http://listofrandomnames.com/index.cfm?generated')

print(conn)