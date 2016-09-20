from django.shortcuts import render

# The functions in this file are referred to as VIEWS
# They all take a request as their input

def index(request):
	name = "Gold Nugget"
	value = 1000.00
	context = {
		"treasure_name": name,
		"treasure_val": value
	}
	return render(request, "index.html", context)
