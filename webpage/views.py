from django.shortcuts import render
from django.utils import timezone

def cooperativa_list(request):
	return render(request, 'webpage/cooperativa_list.html')

def homepage(request):
	return render(request, 'webpage/index.html')

def services(request):
    return render(request, 'webpage/services.html')

def testimony(request):
	return render(request, 'webpage/testimony.html')

def about(request):
	return render(request, 'webpage/about.html')

def contact(request):
	return render(request, 'webpage/contact.html')

def search(request):
	return render(request, 'webpage/search.html')
