from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



engine = create_engine('postgresql://localhost/cs50')
db=scoped_session(sessionmaker(bind=engine))
def main():
     flights=db.execute("SELECT * FROM flights").fetchall()
     for flight in flights:
         print(f"{flight.origin} , {flight.destination}, {flight.duration}")

if __name__=="__main__":
    main()
 