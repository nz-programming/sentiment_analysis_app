from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def engine_creator():
    #set parameter
    dialect = "mysql"
    driver = "pymysql"
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'tanalysis'

    #create engine
    engine = create_engine(f'{dialect}+{driver}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}',
                        encoding='utf-8', echo=True)
    return engine

def create_session():
    Session = sessionmaker(bind=engine_creator())
    return Session()