import requests
import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACE_API')
print(GOOGLE_API_KEY)


LOCATION_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json"

location_parameters = {
    "address": "3500 East Frank Phillips Blvd, Bartlesville, OK",
    "key": GOOGLE_API_KEY

}

location_raw_data = requests.get(LOCATION_ENDPOINT, params=location_parameters)
location_raw_data.raise_for_status()
location_data = location_raw_data.json()
print(location_data)
