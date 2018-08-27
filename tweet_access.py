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

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print(json.dumps(result._json, indent=4))
    
for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.followers_count)
    print(status.place)