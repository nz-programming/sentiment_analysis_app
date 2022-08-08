import pandas as pd
from collect_data import collect_tweets
import datetime
from nltk.corpus import stopwords
import html
import string
import re
from nltk import word_tokenize
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import numpy as np

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

    # create dateframe for polality_json
    df_tweets_pol = pd.DataFrame([t['full_text'] for t in tweets], columns=['text'])
    df_tweets_pol['user_screen_name'] = [t['user']['screen_name'] for t in tweets]
    df_tweets_pol['profile_img'] = [t['user']['profile_image_url_https'] for t in tweets]
    df_tweets_pol['sentiment_score'] = df_tweets_pol['text'].apply(text_cleanup).apply(sentim_polarity)
    df_tweets_pol['create_date'] = [t['created_at'] for t in tweets]
    df_tweets_pol['create_date'] = df_tweets_pol['create_date'].apply(time_transform)
    
    polality_json = df_tweets_pol.sort_values(by='sentiment_score', ascending=False).head(5).to_json()


    #create dataframe for retweet_json 
    df_tweets_ret = pd.DataFrame([t['full_text'] for t in tweets], columns=['text'])
    df_tweets_ret['user_screen_name'] = [t['user']['screen_name'] for t in tweets]
    df_tweets_ret['profile_img'] = [t['user']['profile_image_url_https'] for t in tweets]
    df_tweets_ret['num_retweet'] = [t['retweet_count'] for t in tweets]
    df_tweets_ret['create_date'] = [t['created_at'] for t in tweets]
    df_tweets_ret['create_date'] = df_tweets_ret['create_date'].apply(time_transform)
    
    retweet_json = df_tweets_ret.sort_values(by='num_retweet', ascending=False).head(5).to_json()


    #count keywords
    def all_text():
        conbined_text = ' '.join(df_tweets_pol['text'].apply(text_cleanup))
        return conbined_text

    keywords = WordCloud().process_text(all_text())
    df_keywords = pd.DataFrame(list(keywords.items()), columns=['keyword', 'count']).set_index('keyword')
    df_keywords = df_keywords.sort_values(by="count", ascending=False).head(5)
    keyword_json = df_keywords.to_json()
    print(f"keyword_json:{keyword_json}")


    #count keyphrases
    text_test = df_tweets_pol['text'].apply(text_cleanup)
    bigram_finder = nltk.BigramCollocationFinder.from_documents([d.split() for d in text_test])
    bigram_freq = list(bigram_finder.ngram_fd.items())

    df_keyphrase = pd.DataFrame([(' '.join(k), v) for k,v in bigram_freq], columns=['keyphrase', 'count']).set_index('keyphrase')
    df_keyphrase = df_keyphrase.sort_values(by='count', ascending=False).head(5)
    keyphrase_json = df_keyphrase.to_json()
    print(f"keyphrase_json:{keyphrase_json}")


    #number tweet
    num_tweet = len(tweets)
    print(num_tweet)


    #average polality
    average_polality = df_tweets_pol['sentiment_score'].mean()
    print(average_polality)


    #create a wordcloud
    wc = WordCloud(width=1200, height=800, max_font_size=110, collocations=False).generate(all_text())
    wordcloud = str(wc.to_array())
    print(wordcloud)
    # wordcloud = wc.to_file(f'{datetime.date.today()}.jpg')
    # file_wc_2 = wc.to_file
    # print(file_wc_1)
    # print(file_wc_2)
    # plt.axis("off")
    # plt.imshow(wc, interpolation="bilinear")
    # plt.show()




    return(polality_json, retweet_json, keyword_json, keyphrase_json, wordcloud, num_tweet, average_polality)


