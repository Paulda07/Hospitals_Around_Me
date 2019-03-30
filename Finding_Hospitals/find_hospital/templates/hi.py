import googlemaps
import pprint
import time
# from GoogleMapsAPIKey import get_my_key

API_KEY = 'AIzaSyCUZr_tB1ctwnIDIujJAMvM3SCRGlAEefg'

gmaps = googlemaps.Client(key = API_KEY)

places_result = gmaps.places_nearby (location = '17.4283104, 78.53861010000003', radius = 15000, open_now = False, type = 'hospital')
# pprint.pprint(places_result)

# time.sleep(3)
# places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])
place_list = []
for place in places_result['results']:
	my_place_id = place['place_id']
	my_fields = ['name', 'formatted_phone_number', 'formatted_address']
	place_details =gmaps.place(place_id = my_place_id, fields = my_fields)
	place_list.append(place_details['result'])
#print(place_list)
obj = place_list[0]
print(obj['form'])
# for i in places_result['results']:
# 	# for place in i['result']:
# 	print (i)
#print (List)