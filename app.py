from flask import Flask, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from datetime import datetime , date, time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '4ab95f1aa482c51eddcdde912a6270a3059bfce022f34a834203543d35'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///liga.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#zmniejsza zużycie pamięci - wyłącza info o zmianach

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True)
    name = db.Column(db.Integer)
    surname = db.Column(db.Integer, index = True)
    contractType = db.Column(db.Integer) #How many hours to work in month
    email = db.Columnt(db.String)

class Month(db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True)
    date = db.Column(db.Date)
    days = db.Column(db.PickleType default = [])

class new_diagram_form(FlaskForm):
    month = SelectField('Proszę wybrać miesiąc: ', validators=[DataRequired()], choices=[1 - 12])
    submit = SubmitField('Dalej')


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/new_diagram', methods = ['GET', 'POST']
def new_diagram():
    form = new_diagram_form()
    return render_template('new_diagram.html', form = form)
