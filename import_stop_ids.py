import os
import requests

from cs50 import SQL

db = SQL("sqlite:///bus.db")

api_key = os.environ.get("API_KEY")

# documentation: http://developer.onebusaway.org/modules/onebusaway-application-modules/current/
STOP_IDS_URL = f"https://bustime.mta.info/api/where/stop-ids-for-agency/MTA.json?key={api_key}"

def populate_stop_ids():
    response = requests.get(STOP_IDS_URL)
    if response.status_code == 200:
        stop_ids = response.json()["data"]["list"]
    for stop_id in stop_ids:
        db.execute("INSERT INTO stops (stop_id) VALUES (?)", stop_id)

    else:
        print(f"Error fetching stop IDS: {response.status_code}")

if __name__ == "__main__":
    populate_stop_ids()
