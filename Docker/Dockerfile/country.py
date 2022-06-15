from geopy.geocoders import Nominatim


def get_country_name(place):
    nom = Nominatim(user_agent="My-Application")
    location = nom.geocode(place, addressdetails=True)
    if location is None:
        return ""
    if 'country' in location.raw['address'].keys():
        return location.raw['address']['country']
    else:
        return ""


