from django.shortcuts import render
from django.utils import timezone
# from .models import Cooperativa

def cooperativa_list(request):
	return render(request, 'webpage/cooperativa_list.html')

def homepage(request):
	return render(request, 'webpage/index.html')

<<<<<<< HEAD
def servicios(request):
	return render(reuest, 'webpage/services.html')
=======
def services(request):
    return render(request, 'webpage/services.html')
>>>>>>> 5ce575a782873dda6d052d1edceeba3dd535b90c
