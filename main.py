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

    try:
        location_raw_data = requests.get(
            LOCATION_ENDPOINT, params=location_parameters)
        location_raw_data.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)  # placeholder - redirect to a 404 page
    else:
        location_data = location_raw_data.json()
        if location_data['status'] == 'ZERO_RESULTS':
            print("NO RESULTS FOUND!!")  # placeholder - redirect to a 404 page
            return False
        else:
            latitude = location_data['results'][0]['geometry']['location']['lat']
            longitude = location_data['results'][0]['geometry']['location']['lng']
            return (latitude, longitude)


loc = user_geocode()
print(loc)
