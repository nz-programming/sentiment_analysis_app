from map_data import map_data_db
import connect_db

def extract_dbdata():
    session = connect_db.create_session()
    all_data = session.query(map_data_db).order_by(map_data_db.id).all()

    for d in all_data:
        print(d.id, d.polality_joson, d.retweet_json, d.keyword_count, d.keyphrase_count, d.wordcloud, d.number_tweet, d.average_polality, d.date)

if __name__ == '__main__':
    extract_dbdata()