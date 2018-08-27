import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'xLs1QHhgPuk3hndukwNPqNAi2'
CONSUMER_SECRET = 'ZLzsz6YTDmJ4QyeAG1OiEQwGxboo5zkaeTfQy1rRUpL9seWl81'
OAAUTH_TOKEN = '1008706884881338368-5Rx6PoFnAghebYgUSd12AXEX5Z6zfd'
OAAUTH_TOKEN_SECRET = 'sCzA8KVGvVMRfL8jls98UTSLUaaPXvuH1TyqeAA2Q68bV'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAAUTH_TOKEN, OAAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name'] for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name'] for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)