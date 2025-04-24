import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDTSXje9oiQUb1CzLcq6t48Y0FYRicsWys')
geocode_result = gmaps.geocode('UMD')

print(geocode_result[0]['geometry']['location'])