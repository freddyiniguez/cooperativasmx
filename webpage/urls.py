from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
	url(r'^$', views.homepage, name="homepage"),
	url(r'^servicios$', views.services, name="services"),
	url(r'^testimonios$', views.testimony, name="testimony"),
	url(r'^acerca$', views.about, name="about"),
	url(r'^contacto$', views.contact, name="contact"),
	url(r'^busqueda$', views.search, name="search"),
]