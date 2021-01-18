from django.urls import path
from . import views

app_name = 'jutsu'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anime_id>/', views.character, name='detail_char'),
    path('<str:genre_name>', views.genres, name='index')
]