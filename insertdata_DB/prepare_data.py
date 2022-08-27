from config import *
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

def prepare_dataframe(SEARCH_WORD, NUMBER_TWEET):
    query = f'{SEARCH_WORD} {QUERY_OPERATOR}'

    # import collect data
    tweets = collect_tweets(query, NUMBER_TWEET)


    # transform created_at into edt 
    def time_transform(created_at):
        time_utc = datetime.datetime.strptime(created_at, TIME_FORMAT_TWITTER)
        time_edt = time_utc.astimezone(datetime.timezone(datetime.timedelta(hours = TIME_DIFFERENCE)))
        timestamp_edt = datetime.datetime.strftime(time_edt, TIME_FORMAT)
        return timestamp_edt


    #clean up text
    stop_words = set(stopwords.words(STOPWORDS_LANGUAGE))
    original_stop_words = ORIGINAL_STOP_WORDS
    def text_cleanup(s):
        s_unesc = html.unescape(re.sub(r"http\S+", "", re.sub('\n+', ' ', s)))
        s_noemoji = s_unesc.encode(CHARACTER_CODE, ERROR_ARGUMENT).decode(CHARACTER_CODE)
        wt = word_tokenize(s_noemoji.lower())
        wt_filt = [w for w in wt if (w not in stop_words) and (w not in original_stop_words) and (w not in string.punctuation) and (w.isalnum())]
        return ' '.join(wt_filt)


    #calculate polality
    def sentim_polarity(s):
        return TextBlob(s).sentiment.polarity

    # create dateframe for polality_json
    df_tweets_pol = pd.DataFrame([t[TWEET_TEXT] for t in tweets], columns=[POLALITY_JSON_TEXT])
    df_tweets_pol[POLALITY_JSON_USERNAME] = [t[TWEET_USER][TWEET_USERNAME] for t in tweets]
    df_tweets_pol[POLALITY_JSON_PROFIMAGE] = [t[TWEET_USER][TWEET_PROFIMAGE] for t in tweets]
    df_tweets_pol[POLALITY_JSON_SENTIMENTSCORE] = df_tweets_pol[POLALITY_JSON_TEXT].apply(text_cleanup).apply(sentim_polarity)
    df_tweets_pol[POLALITY_JSON_CREATEDATE] = [t[TWEET_CREATEDATE] for t in tweets]
    df_tweets_pol[POLALITY_JSON_CREATEDATE] = df_tweets_pol[POLALITY_JSON_CREATEDATE].apply(time_transform)
    
    polality_json = df_tweets_pol.sort_values(by = POLALITY_JSON_SENTIMENTSCORE, ascending = False).head(5).to_json()


    #create dataframe for retweet_json 
    df_tweets_ret = pd.DataFrame([t[TWEET_TEXT] for t in tweets], columns=[RETWEET_JSON_TEXT])
    df_tweets_ret[RETWEET_JSON_USERNAME] = [t[TWEET_USER][TWEET_USERNAME] for t in tweets]
    df_tweets_ret[RETWEET_JSON_PROFIMAGE] = [t[TWEET_USER][TWEET_PROFIMAGE] for t in tweets]
    df_tweets_ret[RETWEET_JSON_NUMBER_RETWEET] = [t[TWEET_NUMBER_RETWEET] for t in tweets]
    df_tweets_ret[RETWEET_JSON_CREATEDATE] = [t[TWEET_CREATEDATE] for t in tweets]
    df_tweets_ret[RETWEET_JSON_CREATEDATE] = df_tweets_ret[RETWEET_JSON_CREATEDATE].apply(time_transform)
    
    retweet_json = df_tweets_ret.sort_values(by = RETWEET_JSON_NUMBER_RETWEET, ascending = False).head(5).to_json()


    #count keywords
    def all_text():
        conbined_text = ' '.join(df_tweets_pol[POLALITY_JSON_TEXT].apply(text_cleanup))
        return conbined_text

    keywords = WordCloud().process_text(all_text())
    df_keywords = pd.DataFrame(list(keywords.items()), columns=[KEYWORDCOUNT_JSON_KEYWORD, KEYWORDCOUNT_JSON_COUNT]).set_index(KEYWORDCOUNT_JSON_KEYWORD)
    df_keywords = df_keywords.sort_values(by = KEYWORDCOUNT_JSON_KEYWORD, ascending = False).head(5)
    keyword_json = df_keywords.to_json()


    #count keyphrases
    text_test = df_tweets_pol[POLALITY_JSON_TEXT].apply(text_cleanup)
    bigram_finder = nltk.BigramCollocationFinder.from_documents([d.split() for d in text_test])
    bigram_freq = list(bigram_finder.ngram_fd.items())

    df_keyphrase = pd.DataFrame([(' '.join(k), v) for k,v in bigram_freq], columns=[KEYPHRASECOUNT_JSON_KEYPHRASE, KEYPHRASECOUNT_JSON_COUNT]).set_index(KEYPHRASECOUNT_JSON_KEYPHRASE)
    df_keyphrase = df_keyphrase.sort_values(by = KEYPHRASECOUNT_JSON_COUNT, ascending = False).head(5)
    keyphrase_json = df_keyphrase.to_json()


    #number tweet
    number_tweet = len(tweets)


    #average polality
    average_polality = df_tweets_pol[POLALITY_JSON_SENTIMENTSCORE].mean()


    #create a clean text
    clean_text = all_text()


    return(polality_json, retweet_json, keyword_json, keyphrase_json, clean_text, number_tweet, average_polality)


