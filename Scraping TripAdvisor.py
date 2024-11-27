# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Extract the HTML and create a BeautifulSoup object.
url = 'https://www.tripadvisor.in/Hotels-g28932-Hawaii-Hotels.html'

user_agent = ({'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})


def get_page_contents(url):
    page = requests.get(url, headers=user_agent)
    return BeautifulSoup(page.text, 'html.parser')


soup = get_page_contents(url)

# Find and extract data elements.
hotels = []
for name in soup.findAll('div',{'class':'listing_title'}):
    hotels.append(name.text.strip())
ratings = []
for rating in soup.findAll('a',{'class':'ui_bubble_rating'}):
    ratings.append(rating['alt'])
reviews = []
for review in soup.findAll('a',{'class':'review_count'}):
    reviews.append(review.text.strip())
prices = []
for p in soup.findAll('div',{'class':'price-wrap'}):
    prices.append(p.text.replace('₹','').strip())

# Create the dictionary.
dict = {'Hotel Names':hotels,'Ratings':ratings,'Number of Reviews':reviews,'Prices':prices}

# Create the dataframe.
hawaii = pd.DataFrame.from_dict(dict)
hawaii.head(10)

print(dict)
