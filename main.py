# Import the libraries.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint
"""
# Extract the HTML and create a BeautifulSoup object.
url = 'https://www.tripadvisor.in/Attraction_Products-g155019-Toronto_Ontario.html'

user_agent = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
           'Accept-Language': 'en-US, en;q=0.5'})


def get_page_contents(url):
    page = requests.get(url, headers=user_agent)
    return BeautifulSoup(page.text, 'html.parser')


soup = get_page_contents(url)
print(soup)

# Find and extract data elements.
hotels = []
for name in soup.findAll('div', {'class': 'listing_title'}):
    hotels.append(name.text.strip())
ratings = []
for rating in soup.findAll('a', {'class': 'ui_bubble_rating'}):
    ratings.append(rating['alt'])
reviews = []
for review in soup.findAll('a', {'class': 'review_count'}):
    reviews.append(review.text.strip())
prices = []
for p in soup.findAll('div', {'class': 'price-wrap'}):
    prices.append(p.text.replace('₹', '').strip())

# Create the dictionary.
dict = {'Attraction Names': hotels, 'Ratings': ratings, 'Number of Reviews': reviews, 'Prices': prices}

# Create the dataframe.
hawaii = pd.DataFrame.from_dict(dict)
hawaii.head(10)

pprint.pprint(dict)
"""

url = 'https://www.tripadvisor.in/Attraction_Products-g155019-Toronto_Ontario.html'

response = requests.get(url, headers={'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

items = soup.find_all('span', {'name': 'title'})

pprint.pprint(items)

hotels = []
for name in soup.findAll('div', {'class': 'listing_title'}):
    hotels.append(name.text.strip())
ratings = []
for rating in soup.findAll('a', {'class': 'ui_bubble_rating'}):
    ratings.append(rating['alt'])
reviews = []
for review in soup.findAll('a', {'class': 'review_count'}):
    reviews.append(review.text.strip())
prices = []
for p in soup.findAll('div', {'class': 'price-wrap'}):
    prices.append(p.text.replace('₹', '').strip())

# Create the dictionary.
dict = {'Attraction Names': hotels, 'Ratings': ratings, 'Number of Reviews': reviews, 'Prices': prices}

# Create the dataframe.
hawaii = pd.DataFrame.from_dict(dict)
hawaii.head(10)

pprint.pprint(dict)
