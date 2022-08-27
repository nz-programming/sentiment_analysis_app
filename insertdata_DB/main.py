from config import *
from prepare_data import prepare_dataframe
import datetime
import tweet_add

def get_data():
    polality_json, retweet_json, keyword_json, keyphrase_json, clean_text, number_tweet, average_polality = prepare_dataframe(SEARCH_WORD, NUMBER_TWEET)

    clean_text = clean_text.encode(CLEANTEXT_CHARACTER_CODE)
    date = datetime.date.today()
    
    tweet_add.add_tweet(polality_json, retweet_json, keyword_json, keyphrase_json, clean_text, number_tweet, average_polality, date)


if __name__ == '__main__':
    get_data()