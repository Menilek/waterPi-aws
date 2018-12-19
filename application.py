from waterPi import *
from flask import render_template, request, redirect, url_for
from db import *

@application.route("/", methods=['GET', 'POST'])
def index():
    data = getLastReadingFromDB()    
    return render_template('view.html', items=data)

@application.route("/newReading", methods=['POST'])
def newReading():
    if request.method == 'POST':
        newEntryData = newEntry()
        insertNewReadingToDB(newEntryData)
        data = getLastReadingFromDB()
        return render_template('view.html', items=data)
        #return redirect(url_for('index'))