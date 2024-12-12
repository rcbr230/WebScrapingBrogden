# import urllib.request    Cannot use since I need to be a user-agent 
import requests
from fake_useragent import UserAgent

# urlInput = input() # take in a URL from the user
urlInput = 'https://www.amazon.com/s?k=ass+sex+toy&crid=IAP54QZNM2DH&sprefix=ass+sex+toy%2Caps%2C73&ref=nb_sb_noss'

# simulate a user agent
ua = UserAgent()
randomUA = ua.random
header = {
    'user-agent' : str(randomUA)
    }
print('Header: ' + header['user-agent'])

# get the page using the URL and a header that contains a fake user-agent
page = requests.get(urlInput, headers=header)
htmlContent = page.text

# check for success, otherwise print error code
if page.status_code == 200:
    print(htmlContent)
else:
    print('Status code: ' + str(page.status_code))

# print(htmlContent)