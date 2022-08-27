from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def engine_creator():
    #set parameter
    dialect = DIALECT
    driver = DRIVER
    mysql_user = MYSQL_USER
    mysql_password = MYSQL_PASSWORD
    mysql_host = MYSQL_HOST
    mysql_db = MYSQL_DB

    #create engine
    engine = create_engine(f'{dialect}+{driver}://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}',
                        encoding=ENGINE_CHARACTER_CODE, echo=True)
    return engine

def create_session():
    Session = sessionmaker(bind=engine_creator())
    return Session()