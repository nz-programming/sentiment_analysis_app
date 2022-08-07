import pandas as pd
from collect_data import collect_tweets
import datetime
from nltk.corpus import stopwords
import html
import string
import re
from nltk import word_tokenize
from textblob import TextBlob

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


    #clean up text
    stop_words = set(stopwords.words('english'))
    def text_cleanup(s):
        s_unesc = html.unescape(re.sub(r"http\S+", "", re.sub('\n+', ' ', s)))
        s_noemoji = s_unesc.encode('ascii', 'ignore').decode('ascii')
        wt = word_tokenize(s_noemoji.lower())
        
        wt_filt = [w for w in wt if (w not in stop_words) and (w not in string.punctuation) and (w.isalnum())]
        
        return ' '.join(wt_filt)


    #calculate polality
    def sentim_polarity(s):
        return TextBlob(s).sentiment.polarity

    # create dateframe
    df_tweets = pd.DataFrame([t['full_text'] for t in tweets], columns=['text'])
    df_tweets['user_screen_name'] = [t['user']['screen_name'] for t in tweets]
    df_tweets['profile_img'] = [t['user']['profile_image_url_https'] for t in tweets]
    df_tweets['num_retweet'] = [t['retweet_count'] for t in tweets]
    df_tweets['create_date'] = [t['created_at'] for t in tweets]
    df_tweets['create_date'] = df_tweets['create_date'].apply(time_transform)
    df_tweets['sentiment_score'] = df_tweets['text'].apply(text_cleanup).apply(sentim_polarity)

    return(df_tweets.sort_values(by='sentiment_score', ascending=False).head(5))


