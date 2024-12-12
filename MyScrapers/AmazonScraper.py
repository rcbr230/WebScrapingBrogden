"""
Author:  Reece Brogden
Date:    December 12, 2024
Purpose: Scrape HTML from amazon, and print out all the links and prices in console. As well as store 
            results in a csv file. 
"""


# import urllib.request    Cannot use since I need to be a user-agent 
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# urlInput = input() # take in a URL from the user
urlInput = 'https://www.amazon.com/s?k=dave&i=stripbooks&crid=10HC1FJO3TGCV&sprefix=dave%2Cstripbooks%2C179&ref=nb_sb_noss_2'

# simulate a user agent
ua = UserAgent()
randomUA = ua.random
# NOTE: Amazon requires a User-Agent AND an Accept-Language!!
header = {
    'User-Agent' : str(randomUA),
    'Accept-Language' : 'en-US, en;q=0.5'
    }
print('Header: ' + header['User-Agent'])

# get the page using the URL and a header that contains a fake user-agent
page = requests.get(urlInput, headers=header)
htmlContent = page.text

# Use beautiful soup to easily find what I am searching for in the HTML
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('span', class_='')

for each in links:
    print(each)

# check for success, otherwise print error code
if page.status_code == 200:
    # print(htmlContent)
    pass
else:
    print('Status code: ' + str(page.status_code))
