import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'xLs1QHhgPuk3hndukwNPqNAi2'
CONSUMER_SECRET = 'ZLzsz6YTDmJ4QyeAG1OiEQwGxboo5zkaeTfQy1rRUpL9seWl81'
OAAUTH_TOKEN = '1008706884881338368-5Rx6PoFnAghebYgUSd12AXEX5Z6zfd'
OAAUTH_TOKEN_SECRET = 'sCzA8KVGvVMRfL8jls98UTSLUaaPXvuH1TyqeAA2Q68bV'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAAUTH_TOKEN, OAAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)