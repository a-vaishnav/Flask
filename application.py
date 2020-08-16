from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

application =Flask(__name__)

engine = create_engine('postgresql://localhost/cs50')
db = scoped_session(sessionmaker(bind=engine))

@application.route('/')
def index():
    flights=db.execute('SELECT * FROM flights').fetchall()
    return render_template('index.html', flights=flights)


@application.route('/Book', methods=['POST'])
def Book():
    try:
        flightid = request.form.get("flightid")
    except ValueError:
        return render_template('err.html', message='Invalid flight number')
    name = request.form.get("name")
    
    if db.execute('SELECT * FROM flights WHERE id=:flight_id',{'flight_id':flightid}).rowcount==0:
        return render_template('err.html', message='No flight found')
    
    db.execute('INSERT INTO passengers (names, flight_id) VALUES (:name,:flight_id)',{'name':name,'flight_id':flightid})
    db.commit()

    return render_template('success.html') 

@application.route('/flights')
def flights():
    allf = db.execute('SELECT * FROM flights').fetchall()
    return render_template('allf.html',allf=allf)

@application.route('/flight/<int:flight_id>')
def flight(flight_id):
    flight= db.execute('SELECT * FROM flights WHERE id=:id', {'id':flight_id}).fetchone()
    if flight is None:
        return render_template('err.html', message='No flight found')
    
    passengers=db.execute('SELECT * FROM passengers WHERE flight_id=:flightid',{'flightid':flight_id}).fetchall()
    return render_template('flight.html', flight=flight, passengers=passengers)

if __name__=="__main__":
    application.run(debug=True)