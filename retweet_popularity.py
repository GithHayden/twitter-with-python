import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter


CONSUMER_KEY = 'xLs1QHhgPuk3hndukwNPqNAi2'
CONSUMER_SECRET = 'ZLzsz6YTDmJ4QyeAG1OiEQwGxboo5zkaeTfQy1rRUpL9seWl81'
OAAUTH_TOKEN = '1008706884881338368-5Rx6PoFnAghebYgUSd12AXEX5Z6zfd'
OAAUTH_TOKEN_SECRET = 'sCzA8KVGvVMRfL8jls98UTSLUaaPXvuH1TyqeAA2Q68bV'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAAUTH_TOKEN, OAAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 150
query = 'Ireland'

# get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10  # the min amount of times a status is retweeted to gain entry to our list
# reset this value to suit your own tastes

pop_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'  # align the columns
print(table)