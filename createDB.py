from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.calcWater import *
from app.waterData import *

application = Flask(__name__)
application.config.from_object('config')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    litres = db.Column(db.Numeric, nullable = False)
    percentage = db.Column(db.Integer, nullable = False)
    created_on = db.Column(db.DateTime, default=datetime.now, index = True)    

    def __init__(self, litres, percentage, created_on=None):
        self.litres = litres
        self.percentage = percentage

db.create_all()

if __name__ == "__main__":
    waterLevel = [0, 0]
    insertNewReadingToDB(waterLevel)