from geopy.geocoders import Nominatim

def get_country_name(place):
    geolocator = Nominatim(user_agent="My-Application")
    location = geolocator.geocode(place, addressdetails=True)
    if location is None:
        return ""
    return location.raw['address']['country']
