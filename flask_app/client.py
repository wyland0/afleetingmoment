import googlemaps

class GoogleClient(object):
    def __init__(self, api_key):
        self.key = api_key
        self.gmaps = googlemaps.Client(key=api_key)

    def getKey(self):
        return self.key
    
    def geocode(self, location):
        loc = self.gmaps.geocode(location)[0]['geometry']['location']
        return (loc['lat'], loc['lng'])