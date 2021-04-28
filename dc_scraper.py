import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import tweepy

# Creating list to append tweet data
tweets_list = []

# Using TwitterSearchScraper to scrape records
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('arrest near:"Washington, D.C." since:2021-01-01 until:2021-04-01').get_items()):
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
tweets_df = pd.DataFrame(tweets_list, columns = ['Datetime', 'Tweet_id', 'Text', 'Username'])

print(tweets_df)
