import os, requests, json

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///bus.db")

api_key = os.environ.get("API_KEY")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    stops = db.execute("SELECT stop_name FROM stops")
    if request.method == "GET":
        return render_template("index.html", stops=stops)
    if request.method == "POST":
        stopName = request.form.get('stopName')
        return redirect(url_for('stopinfo', stopName=stopName))


@app.route("/stopinfo", methods=["GET"])
def stopinfo():
    stopName = request.args.get('stopName', None)

    stops = db.execute("SELECT stop_name FROM stops")

    found = False
    for stop in stops:
        if stop['stop_name'] == stopName:
            found = True

    if not found:
        return render_template("stopnameerror.html")

    stopID = db.execute("SELECT stop_id FROM stops WHERE stop_name = ?", stopName)
    stopID = stopID[0]['stop_id']
    stopNumber = stopID[4:]
    stop_info_url = f"https://bustime.mta.info/api/siri/stop-monitoring.json?key={api_key}&MonitoringRef={stopNumber}"
    response = requests.get(stop_info_url)
    if response.status_code == 200:
        stopData = response.json()

        try:
            busesData = stopData['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']

            bus_info = []

            for bus in busesData:
                MonitoredVehicleJourney = bus['MonitoredVehicleJourney']
                bus_line = MonitoredVehicleJourney['LineRef']
                stops_away = MonitoredVehicleJourney['MonitoredCall']['Extensions']['Distances']['StopsFromCall']

                bus_info.append({'bus_line': bus_line, 'stops_away': stops_away})

        except KeyError:
            bus_info = []
    else:
        print("Error retrieving stop IDs")

    return render_template("stopinfo.html", stopName=stopName, bus_info=bus_info)
