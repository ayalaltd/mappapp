import requests
import googlemaps

api_key = 'AIzaSyD4I0zmGa0P0z2OnpaC7iUpikmDBWCwhIg'
gmaps = googlemaps.Client(key='AIzaSyD4I0zmGa0P0z2OnpaC7iUpikmDBWCwhIg')

# sending get request and saving the response as response object
r = requests.get(
    f'https://maps.googleapis.com/maps/api/geocode/json?place_id=ChIJ8wA55eoNK4cRwdm_2MFhQFE&key= {api_key}')
dr = requests.get(
    f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=33.4721077%2C-112.0261424&destinations=40.659569%2C-73.933783&key=AIzaSyD4I0zmGa0P0z2OnpaC7iUpikmDBWCwhIg')

distance = gmaps.distance_matrix((33.4721077, -112.0261424), (40.659569, -73.933783))

# extracting data in json format
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s"
      % (latitude, longitude))
print(distance)