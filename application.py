from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.calcWater import *
from app.waterData import *

application = Flask(__name__)
application.config.from_object('config')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

@application.route("/", methods=['GET', 'POST'])
def index():
    lastReading = getLastReadingFromDB()
    #percentage = calcPercentageRemaining(lastReading[1])
    #data = [lastReading, percentage] 
    return render_template('view.html', items=lastReading)

@application.route("/newReading", methods=['POST'])
def newReading():
    if request.method == 'POST':
        waterLevel = calcWaterData()
        insertNewReadingToDB(waterLevel)
        return redirect(url_for('index'))

if __name__ == "__main__":
    application.run(host='0.0.0.0')