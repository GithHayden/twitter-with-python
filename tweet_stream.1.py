from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'xLs1QHhgPuk3hndukwNPqNAi2'
CONSUMER_SECRET = 'ZLzsz6YTDmJ4QyeAG1OiEQwGxboo5zkaeTfQy1rRUpL9seWl81'
OAAUTH_TOKEN = '1008706884881338368-5Rx6PoFnAghebYgUSd12AXEX5Z6zfd'
OAAUTH_TOKEN_SECRET = 'sCzA8KVGvVMRfL8jls98UTSLUaaPXvuH1TyqeAA2Q68bV'

keyword_list = ['python', 'javascript', 'php', 'C#'] # track list

limit = 500

class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print("Failed on_data: %s"%str(e))
            return True
        else:
            return False
            
    def on_error(self, status):
        print(status)
        return True
        
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAAUTH_TOKEN, OAAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)