import twitter 

class twitter_api:
    def __init__(self, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.API_KEY = API_KEY
        self.API_KEY_SECRET = API_KEY_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET

        
        self.twitter_account = None
        self.last_tweet_time = None
    
    def reconnect(self):
        self.twitter_account = twitter.Api(consumer_key=self.API_KEY,
                        consumer_secret=self.API_KEY_SECRET,
                        access_token_key=self.ACCESS_TOKEN,
                        access_token_secret=self.ACCESS_TOKEN_SECRET)
        self.twitter_account.tweet_mode = 'extended'

    """
    Returns True if a new time has been set - also indicates that 
    a new notification should be sent.

    Checks the last time a notification was sent and if a new 
    tweet needs to be sent, updates the time
    """
    def set_tweet_time_if_latest(self, time):
        # User posted a new tweet since the last time notification was sent
        if self.last_tweet_time and time > self.last_tweet_time:
            self.last_tweet_time = time
            return True
        
        # User hasn't tweeted anything since the last time notification was sent
        elif self.last_tweet_time:
            return False

        # This is the first time the program ran
        else:
            self.last_tweet_time = time
            return True
    
    """
    Returns latest tweet and the time it was created
    """
    def get_latest_tweet(self):
        latest_tweet = self.twitter_account.GetUserTimeline(count=1)
        latest_tweet = latest_tweet[0]

        time_in_seconds = int(latest_tweet.created_at_in_seconds)  
        tweet_text = latest_tweet.full_text

        return tweet_text, time_in_seconds