from map_data import map_data_db
import connect_db

def add_tweet(polality_json, retweet_json, keyword_json, keyphrase_json, clean_text, number_tweet, average_polality, date):
    session = connect_db.create_session()

    add_tweet_db = map_data_db(polality_joson=polality_json, retweet_json=retweet_json, keyword_count=keyword_json, keyphrase_count=keyphrase_json, clean_text=clean_text, number_tweet=number_tweet, average_polality=average_polality, date=date)
    session.add(add_tweet_db)
    session.commit()