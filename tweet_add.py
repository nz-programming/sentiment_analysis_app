from map_data import map_data_db
import connect_db

def add_tweet(polality_joson, retweet_json, keyword_count, keyphrase_count, wordcloud, number_tweet, average_polality, date):
    session = connect_db.create_session()

    add_tweet_db = map_data_db(polality_joson=polality_joson, retweet_json=retweet_json, keyword_count=keyword_count, keyphrase_count=keyphrase_count, wordcloud=wordcloud, number_tweet=number_tweet, average_polality=average_polality, date=date)
    session.add(add_tweet_db)
    session.commit()