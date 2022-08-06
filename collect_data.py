import tweepy as tw
import config_twitter
import datetime

# set date for search and collect
today = datetime.date.today()
today_year = today.year
today_month = today.month
thismonth_start = datetime.date(today_year, today_month, 1)

if today_month == 1:
    lastmonth_start = datetime.date(today_year-1, 12, 1)
    lastmonth_last = datetime.date(today_year-1, 12, 31)
else:
    lastmonth_start = datetime.date(today_year, today_month-1, 1)
    lastmonth_last = thismonth_start + datetime.timedelta(days=-1)

sinceDate = lastmonth_start
untilDate = lastmonth_last


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
    tweets = [tweet._json for tweet in tw.Cursor(api.search_tweets, q=query, since = sinceDate, until = untilDate, lang="en", tweet_mode='extended').items(ntweets)]
    
    return tweets

