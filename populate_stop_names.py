import os
import requests

from cs50 import SQL

from xml.etree import ElementTree
# https://docs.python.org/3/library/xml.etree.elementtree.html

db = SQL("sqlite:///bus.db")

api_key = os.environ.get("API_KEY")

def populate_stop_names():
    stop_ids = db.execute("SELECT stop_id FROM stops")
    counter = 0
    for stop_id in stop_ids:
        current_id = stop_id["stop_id"]
        api_url = f"https://bustime.mta.info/api/where/stop/{current_id}.xml?key={api_key}"

        response = requests.get(api_url)

        root = ElementTree.fromstring(response.content)

        stop_name = root.find("data").find("name").text
        stop_latitude = root.find("data").find("lat").text
        stop_longitude = root.find("data").find("lon").text

        db.execute("UPDATE stops SET stop_name = ?, latitude = ?, longitude = ? WHERE stop_id = ?", stop_name, stop_latitude, stop_longitude, current_id)

        counter = counter + 1

        print(f"Counter: {counter}")

if __name__ == "__main__":
    populate_stop_names()
