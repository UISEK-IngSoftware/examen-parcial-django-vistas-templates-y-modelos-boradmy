from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:id>/', views.peliculas_details, name='peliculas_details'),
]
