from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Parazit/$', views.film1, name='film1'),
    url(r'^Busan/$', views.film2, name='film2'),
    url(r'^Busan2/$', views.film3, name='film3'),
]