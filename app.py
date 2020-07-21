# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect

# epa0r89txUF9HQLb admin password

# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event": "Project Presentation", "date": "2020-07-31"}
    ]

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'
app.config['MONGO_URI'] = 'mongodb+srv://admin:epa0r89txUF9HQLb@cluster0.80lh6.mongodb.net/test?retryWrites=true&w=majority'


mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    # Connect to the database
    collection = mongo.db.events
    # Limit the amount of responses that you see (can be any amount)
    events = collection.find({})
    # return data to user
    return render_template('index.html', events = events)

# CONNECT TO DB, ADD DATA

@app.route('/add')
def add():
    # connect to the database
    collections = mongo.db.events
    # insert new data
    # collections.insert({"event": "Birthday", "data": "2020-10-04"})
    my_events = list(collections.find({}).sort("date", -1))
    print(my_events)
    # return a message to the user
    return "Event added successfully."

@app.route('/events/new', methods=['GET','POST'])
def new_event():
    if request.method == "GET":
        return render_template('new_events.html')
    else: 
        event_name = request.form["event_name"]
        event_date = request.form["event_date"]
        user_name = request.form['user_name']
        # Connect to a database
        events = mongo.db.events
        # Add to the data base
        events.insert({'event': event_name, "date": event_date, "user": user_name})
        # return redirect('/')