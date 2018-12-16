from waterPi import *
from flask import render_template, request, redirect, url_for
from db import *

# Instantiates index page by requesting and inserting data into
# view.html template file from the PostgreSQL database
@app.route("/", methods=['GET', 'POST'])
def index():
    data = getLastReadingFromDB()    
    return render_template('view.html', items=data)

# When 'NEW READING' button is clicked a new water reading is
# taken and inserted into database and the user is redirected
# to the home page showing the new information
@app.route("/newReading", methods=['POST'])
def newReading():
    if request.method == 'POST':
        newEntryData = newEntry()
        insertNewReadingToDB(newEntryData)
        data = getLastReadingFromDB()
        return render_template('view.html', items=data)
        #return redirect(url_for('index'))   

#Runs the script instantiating the application on the localhost server
#Debug is set to true to produce detailed information on execution in the terminal
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)