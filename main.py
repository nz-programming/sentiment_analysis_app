from prepare_data import prepare_dataframe
import datetime
import tweet_add

# parameter for search and collect
keyword = "lipstick_2"
ntweets = 10


def get_data():
    df_tweets = prepare_dataframe(keyword, ntweets).to_json()
    print(f'main:{df_tweets}')

    polality_joson = df_tweets
    retweet_json = df_tweets
    keyword_count = 5000
    keyphrase_count = 3000
    wordcloud = 'test'.encode('utf-8')
    number_tweet = 5000
    average_polality = 0.15
    date = datetime.date.today()
    tweet_add.add_tweet(polality_joson, retweet_json, keyword_count, keyphrase_count, wordcloud, number_tweet, average_polality, date)


if __name__ == '__main__':
    get_data()