import tweepy as tw
import config_twitter
import datetime

# set date for search and collect
untilDate=datetime.date.today()

# establish an initial API connection
def connect_api_client():
    auth = tw.OAuthHandler(config_twitter.consumer_key, config_twitter.consumer_secret)
    auth.set_access_token(config_twitter.access_token, config_twitter.access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        user = api.verify_credentials()
        if not user:
            raise("Credentials could not be verified: Please check config.py")
        print(f"Connected to Twitter API as {user.name}")
    except Exception as e:
        raise e
        
    return api

def collect_tweets(query, ntweets):
    api = connect_api_client()
    #tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang="en", tweet_mode='extended').items(ntweets)]
    tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang="en", tweet_mode='extended').items()]
    return tweets

