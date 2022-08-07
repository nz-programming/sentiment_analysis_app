from prepare_data import prepare_dataframe
import datetime
import tweet_add

# parameter for search and collect
keyword = "lipstick_2"
ntweets = 10


def get_data():
    polality_json, retweet_json, keyword_json, keyphrase_json, num_tweet, average_polality = prepare_dataframe(keyword, ntweets)
    print(f'main:{polality_json}')
    print(f'main:{retweet_json}')

    polality_json = polality_json
    retweet_json = retweet_json
    keyword_count = keyword_json
    keyphrase_count = keyphrase_json
    wordcloud = 'test'.encode('utf-8')
    number_tweet = num_tweet
    average_polality = average_polality
    date = datetime.date.today()
    tweet_add.add_tweet(polality_json, retweet_json, keyword_count, keyphrase_count, wordcloud, number_tweet, average_polality, date)


if __name__ == '__main__':
    get_data()