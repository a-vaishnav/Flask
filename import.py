import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://localhost/cs50')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open('flights.csv')
    reader = csv.reader(f)
    for orig, dest, dur in reader:
        db.execute('INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)',
        {'origin': orig, 'destination':dest,'duration':dur})
        print(f"Added {orig}, {dest}, {dur}")
    db.commit()

if __name__=='__main__':
    main()