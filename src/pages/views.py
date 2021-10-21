from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):

	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):

	return render(request, "contact.html", {}) #String of HTML code

def about_view(request, *args, **kwargs):

	my_context = {
		"my_text" : "this is about us",
		"my_number":123,
		"my_list": [57,22,124]
	}
	return render(request, "about.html",my_context) #String of HTML code