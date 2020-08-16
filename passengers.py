from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://localhost/cs50')
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute('SELECT * FROM flights').fetchall()
    for flight in flights:
        print(f"Flight {flight.id} : {flight.origin} to {flight.destination} , Time: {flight.duration}")

    flight_id = int(input('Enter flight ID :'))
    flight_pres = db.execute('SELECT * FROM flights WHERE id = :fid', {'fid':flight_id}).fetchone()
     
    if flight_pres is None:
        print('Error: No such flight exist')
    
    passengers = db. execute('SELECT * FROM passengers WHERE flight_id = :flightid', {'flightid':flight_id}).fetchall()

    print('Passengers :')

    if len(passengers)==0:
        print('No passenger')
    for passenger in passengers:
        print(f"{passenger.names}")


if __name__=='__main__':
    main()