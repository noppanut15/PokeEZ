from django.conf.urls import url

from . import views

app_name = 'analytic'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<pokemon_id>[0-9]+)/$', views.detail, name='detail'),
]
