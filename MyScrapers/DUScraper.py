"""
Author:  Reece Brogden
Date:    December 12, 2024
Purpose: Scrape HTML DU Site





NOTE: THIS DOESNT WORK LIKE IT SHOULD. I STOPPED WORKING ON THIS TO DO IT ON JS INSTEAD. SEE DUScraper.js


"""

# import urllib.request    Cannot use since I need to be a user-agent 
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# urlInput = input() # take in a URL from the user
urlInput = 'https://denverpioneers.com/index.aspx'

# simulate a user agent and build header
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
page =          requests.get(urlInput, headers=header)
htmlContent =   page.text


# Use beautiful soup to easily find what I am searching for in the HTML
soup = BeautifulSoup(page.content, 'html.parser')

# grab script on DU site that contains the scoreboard
data = soup.find('h2', id='h2_scoreboard')
data = data.find_next('script')

str_data = str(data)
str_data = str_data[24:len(str_data)-136]

str_data_json = json.loads(str_data)

print(json.dumps(str_data_json))

# check for success, otherwise print error code
if page.status_code == 200:
    # print(htmlContent)
    pass
else:
    print('Status code: ' + str(page.status_code))
