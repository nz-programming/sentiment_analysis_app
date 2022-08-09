from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT, FLOAT, LONGBLOB 

Base = declarative_base()


class map_data_db(Base):
    __tablename__ = 'main'

    id = Column(Integer, primary_key=True)
    polality_joson = Column(LONGTEXT, nullable=False)
    retweet_json = Column(LONGTEXT, nullable=False)
    keyword_count = Column(Integer, nullable=False)
    keyphrase_count = Column(Integer, nullable=False)
    wordcloud = Column(LONGBLOB, nullable=False)
    number_tweet = Column(Integer, nullable=False)
    average_polality = Column(FLOAT, nullable=False)
    date = Column(DATE, nullable=False)