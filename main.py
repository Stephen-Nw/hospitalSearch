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
            return False
        else:
            latitude = location_data['results'][0]['geometry']['location']['lat']
            longitude = location_data['results'][0]['geometry']['location']['lng']
            return (latitude, longitude)


def hospital_search():
    """Locate hospitals within a specified geographical radius using coordinates from the user_geocode function"""
    user_coordinates = user_geocode()

    if user_coordinates != False:
        user_latitude = user_coordinates[0]
        user_longitude = user_coordinates[1]
    else:
        print('ADDRESS NOT FOUND')  # placeholder - redirect to a 404 page
        return False

    try:
        hospital_raw_data = requests.get(
            f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={user_latitude}%2C{user_longitude}&radius=6000&type=hospital&key={GOOGLE_API_KEY}")
        hospital_raw_data.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)  # Placeholder - redirect to a 404 page
    else:
        hospital_data = hospital_raw_data.json()
        # print(hospital_data)
        if hospital_data['status'] == 'ZERO_RESULTS':
            # placeholder - redirect to a 404 page
            print("NO HOSPITALS FOUND!!")
            return False
        else:
            hospital_search_results = hospital_data['results']
            print(len(hospital_search_results))
            return hospital_search_results


# hospital_search()

def hospital_dictionary():
    """Convert hospital list from hospital_search function to dictionary"""
    hospital_attributes = ['Name', 'Address']
    hospitals = hospital_search()

    if hospitals != False:
        temporary_hospital_list = []
        for hospital in hospitals:
            hospital_item = []
            name = hospital['name']
            address = hospital['vicinity']
            # ratings = hospital['rating']
            hospital_item.extend([name, address])
            temporary_hospital_list.append(hospital_item)

        final_hospital_list = []
        for hospital in temporary_hospital_list:
            hospital_dictionary_conversion = dict(
                zip(hospital_attributes, hospital))
            final_hospital_list.append(hospital_dictionary_conversion)

        return final_hospital_list

    else:
        print("THERE ARE NO HOSPITALS AROUND YOUR LOCATION")
        return False


print(hospital_dictionary())
