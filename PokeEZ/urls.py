"""PokeEZ URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pokedex/', views.pokedex, name='pokedex'),
    url(r'^overview/', views.overview, name='overview'),
    url(r'^about-us/', views.about, name='about'),
    url(r'^analytic/', include('analytic.urls')),
    url(r'^search-by-name/', views.search_by_name, name='search'),

]
