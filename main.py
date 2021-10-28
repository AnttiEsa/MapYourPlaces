import csv
from database import Base, db
Base.metadata.create_all(db)

from database.operations import insert_data

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    line_count = 0
    for row in reader:
        if(line_count!=0):
            result = insert_data(name=row[2], address=row[5], city=row[7], capacity=row[10], coordinates_lat=row[11], coordinates_lon=row[12])
            print(f"Inserted row NAME: {row[2]} ADDRESS: {row[5]} CITY: {row[7]} CAPACITY: {row[10]} COORDINATES: {row[11]} {row[12]}")
        line_count+=1