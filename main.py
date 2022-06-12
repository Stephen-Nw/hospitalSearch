import requests
import os
import googlemaps

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

    # gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
    # geocode_result = gmaps.geocode("4996 Princeton Drive, Bartlesville, OK")
    # print(geocode_result)

    user_coordinates = user_geocode()
    user_latitude = user_coordinates[0]
    user_longitude = user_coordinates[1]

    USER_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # search_parameters = {
    #     "location": "36.153980%2C-95.992775",
    #     "radius": 1500,
    #     "type": "hospital",
    #     "key": GOOGLE_API_KEY,
    # }

    search_raw_data = requests.get(
        f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={user_latitude}%2C{user_longitude}&radius=1500&type=hospital&key={GOOGLE_API_KEY}")
    # search_raw_data = requests.get(url=USER_ENDPOINT, params=search_parameters)
    search_raw_data.raise_for_status()
    search_data = search_raw_data.json()

    # print(search_data)
    return search_data


hosp_search = hospital_search()
print(hosp_search)
