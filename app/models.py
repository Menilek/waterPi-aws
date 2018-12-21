from app.init import db
from datetime import datetime

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    litres = db.Column(db.Numeric, nullable = False)
    percentage = db.Column(db.Integer, nullable = False)
    created_on = db.Column(db.DateTime, default=datetime.now, index = True)    

    def __init__(self, litres, percentage, created_on=None):
        self.litres = litres
        self.percentage = percentage