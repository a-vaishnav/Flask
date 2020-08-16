import datetime
from flask import Flask, render_template,request, session
from flask_session import Session
app=Flask(__name__)

app.config["SESSION_PARMANENT"]= False
app.config["SESSION_TYPE"]='filesystem'
Session(app)

@app.route('/')
def index():

    now=datetime.datetime.now()
    newyear=now.month==1 and now.day==1
    headline = "Welcome"
    return render_template('index.html', headline=headline, now=now, newyear=newyear)

@app.route('/david')
def david():
    return render_template('person.html')

@app.route('/<string:name>')
def hello(name ):
    return f"Hello {name}"


@app.route('/friends', methods=['GET', 'POST'])
def friends():
    
    flist=['Mohan', 'Soham', 'Ajit', 'Vinay']        
    if request.method=='POST':
        name=request.form.get('frandzz')
        flist.append(name)

    return render_template('friends.html', flist=flist)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/inherittemplate')
def inherittemplate():
    return render_template('inherit.html')

@app.route('/hey', methods=['POST'])
def hey():
    name=request.form.get('frandzz')
    return render_template('hey.html', name=name)


@app.route('/daily', methods=['POST'])
def daily():
    if session.get('tasks') is None:
        session['tasks']=[]
    if request.method=='POST':
        task=request.form.get('task')
        session['tasks'].append(task)
    return render_template('work.html', tasks=session['tasks'])



if __name__ == "__main__":
    app.run(debug=True)