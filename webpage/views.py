from django.shortcuts import render
from django.utils import timezone

def cooperativa_list(request):
	return render(request, 'webpage/cooperativa_list.html')

def homepage(request):
	return render(request, 'webpage/index.html')

def services(request):
    return render(request, 'webpage/services.html')
