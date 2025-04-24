import googlemaps

class GoogleClient(object):
    def __init__(self, api_key):
        gmaps = googlemaps.Client(key=api_key)