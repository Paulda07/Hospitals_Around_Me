

# Create your views here.
from django.shortcuts import render, redirect
#from django.contrib.gis.geos import fromstr
from django.http import HttpResponse
import requests, json 
from .models import Find_Hosp
import googlemaps
import pprint
import time

global res, API_KEY

longi = '78.53861010000003'
lati = '17.4283104, '
 

API_KEY = 'AIzaSyCUZr_tB1ctwnIDIujJAMvM3SCRGlAEefg'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


def index(request): #the index view
    hosps = Find_Hosp.objects.all() r
    
    if request.method == "POST": #checking if the request method is a POST
        if "Find" in request.POST:
        	
	       	return redirect("results/") 
    return render(request, "index.html") 
   
	gmaps = googlemaps.Client(key = API_KEY)

	places_result = gmaps.places_nearby (location = res, radius = 15000, open_now = False, type = 'hospital')
	# pprint.pprint(places_result)

	# time.sleep(3)
	# places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])
	res = lati+longi
	place_list = []
	for place in places_result['results']:
		my_place_id = place['place_id']
		my_fields = ['name', 'formatted_phone_number', 'formatted_address']
		place_details =gmaps.place(place_id = my_place_id, fields = my_fields)
		place_list.append(place_details['result'])
	#print(place_list)
	for i in range (0, len(place_list)):
		obj = place_list[i]
		if ('formatted_phone_number' in obj):
			hosp_obj = Find_Hosp(latitude = 17.4283104, longitude = 78.53861010000003, name = obj['name'], address = obj['formatted_address'], contact = obj['formatted_phone_number'])
			hosp_obj.save()
	hosp_objs = Find_Hosp.objects.all()

	return render(request, "results.html", {"objs": hosp_objs})
	
          
		    


