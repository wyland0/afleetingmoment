import googlemaps

class GoogleClient(object):
    def __init__(self, api_key):
        self.key = api_key
        self.gmaps = googlemaps.Client(key=api_key)

    def getKey(self):
        return self.key
    
    def geocode(self, location):
        try:
            result = self.gmaps.geocode(location)
            if result and len(result) > 0:
                return result[0]['geometry']['location']
            else:
                return {'lat': 0.0, 'lng': 0.0}
        except Exception as e:
            print(f"Error geocoding location: {e}")
            return {'lat': 0.0, 'lng': 0.0}
