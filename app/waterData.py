from flask_sqlalchemy import SQLAlchemy
from app.init import db
from app.models import Reading

def formatReadingDataForDisplay(data):
    formattedTime = data[0].strftime('%H:%M %d/%m/%Y')
    litres = data[1]
    percent = data[2]
    items = [formattedTime, litres, percent]
    return(items)

def getLastReadingFromDB():
    queryData = db.engine.execute("SELECT date_trunc('second', created_on), litres, percentage FROM Reading ORDER BY id DESC LIMIT 1").first()
    formattedData = formatReadingDataForDisplay(queryData)
    return(formattedData)

def handleError(data):
    db.session.rollback()
    db.session.add(data)
    db.session.flush()

def insertNewReadingToDB(waterData):
    reading = Reading(waterData[0], waterData[1])
    try:
        db.session.add(reading)
        db.session.commit()
        db.session.close()
    except:
        handleError(reading)