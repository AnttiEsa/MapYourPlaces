"""Functions to connect database"""
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
"""Orm classes and orm itself"""
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, load_only
import os

"""To read .env file and its variables"""
from dotenv import load_dotenv
from sqlalchemy.orm.session import Session
"""Finds .env file, loads it to the memory and brings them to this python app"""
load_dotenv()

Base = declarative_base()

class Places(Base):
    """
    Describe the table and its content
    """

    __tablename__ = 'myPlaces'

    id = Column(Integer, primary_key = True)
    name = Column(String(255))
    x = Column(Float)
    y = Column(Float)

    def __repr__(self):
        """String representation of the object"""
        return f"Places (name='{self.name}'"

DATABASE_URL = os.environ['DATABASE_URL']

"""Connects to database, searches database.db file and expects it to be in sql-format"""
db = create_engine(DATABASE_URL)
"""To run SQL-commands"""
Session = sessionmaker(bind=db)