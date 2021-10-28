from database import License, Session
from sqlalchemy import or_

def __get__session():
    return Session()

def insert_data(name, address, city, capacity, coordinates_lon, coordinates_lat):
    new_row = License(name=name, address=address, city=city, capacity=capacity, coordinates_lon = coordinates_lon, 
    coordinates_lat = coordinates_lat)

    db = __get__session()
    """Add a new row to wait for a commit"""
    db.add(new_row)
    """Add a command to database to do the action"""
    db.commit()
    id = new_row.id
    db.close()
    return id

