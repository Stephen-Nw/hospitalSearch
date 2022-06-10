import requests
import os


def user_geocode():
    """Obtain a user's latitude and longitude from a provided address"""

    GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACE_API')

    user_location = input("Enter your address: \n")

    LOCATION_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json"

    location_parameters = {
        "address": user_location,
        "key": GOOGLE_API_KEY

    }

    location_raw_data = requests.get(
        LOCATION_ENDPOINT, params=location_parameters)
    location_raw_data.raise_for_status()
    location_data = location_raw_data.json()

    latitude = location_data['results'][0]['geometry']['location']['lat']
    longitude = location_data['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)


loc = user_geocode()
print(loc)
