

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
res = lati+longi 

API_KEY = 'AIzaSyCUZr_tB1ctwnIDIujJAMvM3SCRGlAEefg'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


def index(request): #the index view
    hosps = Find_Hosp.objects.all() #quering all todos with the object manager
    
    if request.method == "POST": #checking if the request method is a POST
        if "Find" in request.POST:
        	# lat = request.POST['lat']
        	# lon = request.POST['lng']
        	# print(lat, lon)
        	# # text = "hi there" #content
        	# obj = Find_Hosp(title=title, text =text)
	       	# print(obj)
	       	# obj.save()
	       	return redirect("results/") #saving the todo 
	        #task here to email user\
	        #SignUpTask.apply_async(eta= date-datetime.utcnow())
             #reloading the page
        
    return render(request, "index.html") 
    #checking if the request method is a POST
        # if "search" in request.POST: #checking if there is a request to add a todo
        #     lat = request.POST["latitude"] #title
        #     # date = str(request.POST["date"]) #date
        #     lon = request.POST["longitude"] #category
        #     r = requests.get(url + 'query=' + lat +'&key=' + api_key)
        #     x = r.json()
        #     y = x['results']
        #     hos = Find_Hosp( title = lat, text= y )
        #     hos.save()
        #     hosps =Find_Hosp.objects.all()
        #     return redirect ("/results", {'places':hosps})
        #     # for i in range(len(y)):
        #    	# 	print(y[i]['name'])        	
			# nearby_spots = Spot.objects.filter(mpoint__distance_lte = (user_location, D(**desired_radius))).distance(user_location).order_by('distance')[:limit]
			# serializer = SpotWithDistanceSerializer(nearby_spots, many=True)
def results(request):
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
	for i in range (0, len(place_list)):
		obj = place_list[i]
		if ('formatted_phone_number' in obj):
			hosp_obj = Find_Hosp(latitude = 17.4283104, longitude = 78.53861010000003, name = obj['name'], address = obj['formatted_address'], contact = obj['formatted_phone_number'])
			hosp_obj.save()
	hosp_objs = Find_Hosp.objects.all()

	return render(request, "results.html", {"objs": hosp_objs})
	
            # content = title + " -- " + date + " " + category #content
            # Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            # Todo.save() #saving the todo 
            #task here to email user\
            #SignUpTask.apply_async(eta= date-datetime.utcnow())
	        #     return redirect("/") #reloading the page
	        # if "taskDelete" in request.POST: #checking if there is a request to delete a todo
	        #     checkedlist = request.POST["checkedbox"] #checked todos to be deleted
	        #     for todo_id in checkedlist:
	        #         todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
	        #         todo.delete() #deleting todo

		    # """
		    # WITH USE OF GEODJANGO and POSTGIS
		    # https://docs.djangoproject.com/en/dev/ref/contrib/gis/db-api/#distance-queries
		    # """
		    


