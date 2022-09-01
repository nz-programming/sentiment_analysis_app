from config import *
from collect_data_twitterapi.config_twitter import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy as tw
import datetime

# set date for search and collect
untilDate=datetime.date.today() - datetime.timedelta(-7)

# establish an initial API connection
def connect_api_client():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
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
    print(untilDate)
    #tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang = COLLECT_TWEET_LANGUAGE, tweet_mode = COLLECT_TWEET_MODE).items(NUMBER_TWEET)]
    #tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, until = untilDate, lang = COLLECT_TWEET_LANGUAGE, tweet_mode = COLLECT_TWEET_MODE).items()]
    tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, lang = COLLECT_TWEET_LANGUAGE, tweet_mode = COLLECT_TWEET_MODE).items()]
    return tweets

