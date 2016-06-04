from __future__ import unicode_literals
from django.db import models 
from django.utils import timezone


class Trabajador(models.Model):
	nombre 	= models.TextField()
	correo 	= models.EmailField()
	fecha_nac= models.DateTimeField()
	sexo 	= models.TextField()
	lugar_origen = models.TextField()
	habilidades = models.TextField()
