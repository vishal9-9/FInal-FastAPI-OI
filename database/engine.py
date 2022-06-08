from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pymysql

engine = create_engine('mysql+pymysql://root:password@localhost/alex')
Base = declarative_base()
session = Session(bind = engine)

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()