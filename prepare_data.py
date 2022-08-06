import pandas as pd
from collect_data import collect_tweets
import datetime


def prepare_dataframe(keyword, ntweets):
    query = f'{keyword} -filter:retweets'

    # import collect data
    tweets = collect_tweets(query, ntweets)


    # transform created time into edt
    def time_transform(created_at):
        time_utc = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
        time_edt = time_utc.astimezone(datetime.timezone(datetime.timedelta(hours=-4)))
        timestamp_edt = datetime.datetime.strftime(time_edt, '%Y-%m-%d')
        return timestamp_edt

    # create dateframe
    df_tweets = pd.DataFrame([t['full_text'] for t in tweets], columns=['text'])
    df_tweets['user_screen_name'] = [t['user']['screen_name'] for t in tweets]
    df_tweets['profile_img'] = [t['user']['profile_image_url_https'] for t in tweets]
    df_tweets['num_retweet'] = [t['retweet_count'] for t in tweets]
    df_tweets['create_date'] = [t['created_at'] for t in tweets]
    df_tweets['create_date'] = df_tweets['create_date'].apply(time_transform)

    return(df_tweets)


