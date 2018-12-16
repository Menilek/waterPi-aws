from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

#Parses data and changes the format of the datetime
def formatReadingDataForDisplay(data):
    formattedTime = data[0].strftime('%H:%M %d/%m/%Y')
    litres = data[1]
    percent = data[2]
    items = [formattedTime, litres, percent]
    return(items)

#Retrieves the latest row entered into the database
def getLastReadingFromDB():
    queryData = db.engine.execute("SELECT date_trunc('second', created_on), litres, percentage FROM Reading ORDER BY id DESC LIMIT 1").first()
    formattedData = formatReadingDataForDisplay(queryData)
    return(formattedData)

def handleError(data):
    db.session.rollback()
    db.session.add(data)
    db.session.flush()

#Takes a list of data and inserts each element of the list into a column in the table
def insertNewReadingToDB(waterData):
    reading = Reading(waterData[0], waterData[1])
    db.session.add(reading)
    try:
        db.session.commit()
    except exc.IntegrityError:
        handleError(reading)

app = Flask(__name__)
#Heroku db details susceptible to change
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://water:waterPi@localhost:1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#alter table Reading ADD id integer PRIMARY KEY, ADD datetime timestamp [without time zone] NOT NULL, ADD litres numeric NOT NULL, percentage integer NOT NULL
class Reading(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    litres = db.Column(db.Numeric, nullable = False)
    percentage = db.Column(db.Integer, nullable = False)
    created_on = db.Column(db.DateTime, default=datetime.now, index = True)    

    def __init__(self, litres, percentage, created_on=None):
        self.litres = litres
        self.percentage = percentage
