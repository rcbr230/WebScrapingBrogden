"""
Author:  Reece Brogden
Date:    December 12, 2024
Purpose: Scrape HTML from Yahoo!Finance, and print out all the trending stocks in console. As well as store 
            results in a csv file. 
"""


# import urllib.request    Cannot use since I need to be a user-agent 
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# urlInput = input() # take in a URL from the user
urlInput = 'https://finance.yahoo.com/markets/stocks/trending/'

# simulate a user agent
ua = UserAgent()
randomUA = ua.random
# NOTE: Amazon requires a User-Agent AND an Accept-Language!!
#   I gave up on trying to do amazon...
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

# grab all company names that are on the stock page
companies = soup.find_all('div', class_='tw-pl-4 yf-h8l7j7')
# values order:
#   price, change, change %, change AGAIN, change % AGAIN, Volume, Market Cap
values = soup.find_all('fin-streamer')

# format into a dict.
results = {}
comapnyIndex = 0
for company in companies:
    results[company.string] = {
        'Price' : values[comapnyIndex].string,
        'Change' : values[comapnyIndex+1].string,
        'ChangePercent' : values[comapnyIndex+4].string,
        'Volume' : values[comapnyIndex+5].string,
        'Market Cap' : values[comapnyIndex+6].string
    }
    comapnyIndex += 1

for i,j in results.items():
    print(i)
    print(j)

# check for success, otherwise print error code
if page.status_code == 200:
    # print(htmlContent)
    pass
else:
    print('Status code: ' + str(page.status_code))
