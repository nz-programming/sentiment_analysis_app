from config import *
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
            raise(ERROR_MESSAGE)
        print(f"{SUCCESS_MESSAGE} {user.name}")
    except Exception as e:
        raise e
        
    return api

def collect_tweets(query, NUMBER_TWEET):
    api = connect_api_client()
    tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang = COLLECT_TWEET_LANGUAGE, tweet_mode = COLLECT_TWEET_MODE).items(NUMBER_TWEET)]
    #tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang = COLLECT_TWEET_LANGUAGE, tweet_mode = COLLECT_TWEET_MODE).items()]
    return tweets

