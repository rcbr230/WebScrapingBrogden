import tweepy

# App authentication----------------------------------------------------------------
consumerKey = 'BQzDyIjtRHxNqRpoUBzcbHqlx'
consumerSecret = 'Zqfx6EyWf6SiVobb4wUMJuEacqTflRTQb2u8Wiz40g2wpwMrUP'
accessToken = '737527100454772736-TzDFVYuxtiePW461bBhl4y8ab2Gdxlm'
accessSecret = 'oHSVxovkflWLWElUJk3sldMUfXjElijmb0Suv5aAmZOY7'

auth = tweepy.OAuth1UserHandler(
        consumerKey, consumerSecret, 
        accessToken, accessSecret
        )

# v1.1
apiV1 = tweepy.API(auth)

# v2
apiV2 = tweepy.Client(
        consumer_key=consumerKey, consumer_secret=consumerSecret,
        access_token=accessToken, access_token_secret=accessSecret
        )

# App authentication----------------------------------------------------------------

# getting tweets

result = apiV2.get_home_timeline()
for tweet in result:
    print(tweet.text)

for i,j in result.items():
    print(i + " : " + j)