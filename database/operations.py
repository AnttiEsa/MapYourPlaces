import csv

from sqlalchemy.sql.expression import column
from database import Places, Session, sessionmaker
from sqlalchemy import or_
from sqlalchemy.orm import load_only
import pandas as pd

def __get_session():
    return Session()

def insert_data(name, x,y):
    new_row = Places(name=name, x = x, 
    y = y)

    db = __get_session()
    """Add a new row to wait for a commit"""
    db.add(new_row)
    """Add a command to database to do the action"""
    db.commit()
    id = new_row.id
    db.close()
    return id

def get():
    return __get_session().query(Places).all()

def getTable():
    fields = ['name', 'x', 'y']
    return __get_session().query(Places).options(load_only(*fields)).all()

def truncateTable():
    db = __get_session()
    db.query(Places).delete()
    db.commit()

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def columnError(csvFile):
    with open(csvFile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        places = pd.read_csv(csvFile, error_bad_lines=False)

        #Check if the required values are found from the first row
        if {'Name', 'x', 'y'}.issubset(places.columns):
            return False
        else:
            return True

def getRows(csvFile):
    with open(csvFile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        line_count = 0

        places = pd.read_csv(csvFile, error_bad_lines=False)
        name_id = -1
        x_id    = -1
        y_id    = -1

        for row in reader:

            if(line_count==0):
                i=0
                for columnName in places.columns:
                    if(columnName == "Name"):
                        name_id = i
                    elif(columnName == "x"):
                        x_id = i
                    elif(columnName == "y"):
                        y_id = i
                    i+=1

            else:
                if(is_float(row[x_id]) and is_float(row[y_id])):
                        if(float(row[x_id]) > -90 and float(row[x_id]) < 90 and float(row[y_id]) > -180 and float(row[y_id]) < 180):
                                insert_data(name=row[name_id], x=row[x_id], y=row[y_id])
            line_count+=1