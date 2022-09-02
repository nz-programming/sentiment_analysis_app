# searching tweet config
SEARCH_WORD = "WORLD CUP OR World Cup OR World cup OR world cup OR WORLDCUP OR WorldCup OR Worldcup OR worldcup"
QUERY_OPERATOR = "-filter:retweets"
NUMBER_TWEET = 100000

# collect tweet
COLLECT_TWEET_LANGUAGE = "en"
COLLECT_TWEET_MODE = "extended"

# access twitter api
ERROR_MESSAGE = "Credentials could not be verified: Please check config.py"
SUCCESS_MESSAGE = "Connected to Twitter API as"

#set time (Eastern Daylight Time)
TIME_FORMAT_TWITTER = "%a %b %d %H:%M:%S +0000 %Y"
TIME_DIFFERENCE = -4  
TIME_FORMAT = "%Y-%m-%d"

# clean text
STOPWORDS_LANGUAGE = "english"
ORIGINAL_STOP_WORDS = ['WORLD', 'CUP', 'World', 'Cup', 'world', 'cup', 'WORLDCUP', 'WorldCup', 'Worldcup', 'worldcup', 'FIFA', 'fifa', '2022', '22']
CHARACTER_CODE = "ascii"
ERROR_ARGUMENT = "ignore"

# create polality_json
TWEET_TEXT =  "full_text"
TWEET_USER = "user"
TWEET_USERNAME = "screen_name"
TWEET_PROFIMAGE = "profile_image_url_https"
TWEET_CREATEDATE = "created_at"
POLALITY_JSON_TEXT = "text"
POLALITY_JSON_USERNAME = "user_screen_name"
POLALITY_JSON_PROFIMAGE = "profile_img"
POLALITY_JSON_SENTIMENTSCORE = "sentiment_score"
POLALITY_JSON_CREATEDATE = "create_date"

# create retweet_json
TWEET_NUMBER_RETWEET = "retweet_count"
RETWEET_JSON_TEXT = "text"
RETWEET_JSON_USERNAME = "user_screen_name"
RETWEET_JSON_PROFIMAGE = "profile_img"
RETWEET_JSON_NUMBER_RETWEET = "num_retweet"
RETWEET_JSON_CREATEDATE = "create_date"

# create keyword_count_json
KEYWORDCOUNT_JSON_KEYWORD = "keyword"
KEYWORDCOUNT_JSON_COUNT = "count"

# create keyphrase_count_json
KEYPHRASECOUNT_JSON_KEYPHRASE = "keyphrase"
KEYPHRASECOUNT_JSON_COUNT = "count"

# encode clean text
CLEANTEXT_CHARACTER_CODE = "utf-8"

# connect db
DIALECT = "mysql"
DRIVER = "pymysql"
MYSQL_USER = "root"
MYSQL_PASSWORD = "admin"
MYSQL_HOST = "localhost"
MYSQL_DB = "tanalysis"
ENGINE_CHARACTER_CODE = "utf-8"

# map database
DB_TABLENAME = "main"