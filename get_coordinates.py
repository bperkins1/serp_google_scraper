from geopy.geocoders import Nominatim

def get_coordinates(query):
    #get coordinates of your location query
    geolocator = Nominatim(user_agent="bizFinderApp")
    location = geolocator.geocode(query)
    latitude = location.latitude
    longitude = location.longitude

    return latitude, longitude
