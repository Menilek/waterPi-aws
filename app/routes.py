from app.init import *
from app.calcWater import *
from app.waterData import *
from flask import render_template, request, redirect, url_for

@app.route("/", methods=['GET', 'POST'])
def index():
    lastReading = getLastReadingFromDB()
    #percentage = calcPercentageRemaining(lastReading[1])
    #data = [lastReading, percentage] 
    return render_template('view.html', items=lastReading)

@app.route("/newReading", methods=['POST'])
def newReading():
    if request.method == 'POST':
        waterLevel = calcWaterData()
        insertNewReadingToDB(waterLevel)
        return redirect(url_for('index'))