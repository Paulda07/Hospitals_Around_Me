

# Create your views here.
from django.shortcuts import render, redirect
#from django.contrib.gis.geos import fromstr
from django.http import HttpResponse
import requests, json 
from .models import Find_Hosp


api_key = 'AIzaSyAmaMvFLcdEXUJd_j5goI-dZfvflEeQj_A'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


def index(request): #the index view

    if request.method == "POST": #checking if the request method is a POST
        if "search" in request.POST: #checking if there is a request to add a todo
            lat = request.POST["latitude"] #title
            # date = str(request.POST["date"]) #date
            lon = request.POST["longitude"] #category
            r = requests.get(url + 'query=' + lat +'&key=' + api_key)
            x = r.json()
            y = x['results']
            print(y)
            hos = Find_Hosp( title = lat, text= y )
            hos.save()
            hosps =Find_Hosp.objects.all()
            return redirect ("/results", {'places':hosps})
            # for i in range(len(y)):
           	# 	print(y[i]['name'])
           	
    return render(request, "index.html")
			# nearby_spots = Spot.objects.filter(mpoint__distance_lte = (user_location, D(**desired_radius))).distance(user_location).order_by('distance')[:limit]
			# serializer = SpotWithDistanceSerializer(nearby_spots, many=True)
			
			
def results(request):
	return render (request, "results.html")
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
		    


