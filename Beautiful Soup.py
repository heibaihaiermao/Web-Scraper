import requests

from bs4 import BeautifulSoup as bs


r = requests.get('https://www.projectpro.io/')


soup = bs(r.content,features="lxml")


header = soup.find_all('a')
print(header)
