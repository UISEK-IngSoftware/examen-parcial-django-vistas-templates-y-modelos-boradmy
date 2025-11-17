from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'index.html', {'peliculas': peliculas})

def peliculas_details(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'peliculas_details.html', {'pelicula': pelicula})
