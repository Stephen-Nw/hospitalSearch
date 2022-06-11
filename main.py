import requests
import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACE_API')


def user_geocode():
    """Obtain a user's latitude and longitude from a provided address"""

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


# loc = user_geocode()
# print(loc)


def hospital_search():
    USER_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    search_parameters = {
        "location": (36.751117, -95.91744450000002),
        "key": GOOGLE_API_KEY,
        "type": "hospital",
        "rankby": "distance"

    }

    search_data = requests.get(USER_ENDPOINT, params=search_parameters)
    search_data.raise_for_status()
    print(search_data)
    return
