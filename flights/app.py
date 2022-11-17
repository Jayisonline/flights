from flask import Flask, render_template, request
from cs50 import SQL, sql
from werkzeug.serving import run_simple
from datetime import datetime



app = Flask(__name__)
# TEMPLATES_AUTO_RELOAD = True
# app.config.from_mapping(config)


# list = "jay"
all_flights = []
list = []

db = SQL("sqlite:///file.db")


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/greet")
def greet():
    return render_template("greet.html")



@app.route("/flights", methods = ["POST"])
def flights():

    start = request.form.get("from")
    to = request.form.get("to")

    list = db.execute("SELECT * FROM flights WHERE origin = ?", start)

    return render_template("show_flights.html", list = list)



@app.route("/all_flights")
def all_flights():
    all_flights = db.execute("SELECT * FROM flights")
    return render_template("all_flights.html", all_flights = all_flights)




@app.route("/done", methods = ["POST"])
def done():
    start = request.form.get("from")
    to = request.form.get("to")
    flight_id = request.form.get("flight_id")
    time = request.form.get("time")
    db.execute("INSERT INTO flights (origin, destination, duration, time) VALUES ( ?, ?, ?, ?)", start, to, flight_id, time)

    return render_template("done.html")
