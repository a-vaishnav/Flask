from models import *
from flask import Flask

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://localhost/lecture4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

def main():
    flights=Flight.query.all()
    for flight in flights:
        print(f"from {flight.origin} to {flight.destination} in {flight.duration}")

if __name__=="__main__":
    with app.app_context():
        main()

