from django.shortcuts import render
from django.http import HttpResponse

# The functions in this file are referred to as VIEWS
# They all take a request as their input

def index(request):
	return HttpResponse("<h1>Hello Explorers!</h1>")