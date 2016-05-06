from app import app
from flask import render_template
from getBuses import getBuses

@app.route('/')
@app.route('/index')
def index():
    busList = getBuses()
    return render_template('index.html',busList=busList)
