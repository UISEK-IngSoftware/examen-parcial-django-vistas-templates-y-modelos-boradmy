from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio_lanzamiento = models.IntegerField()
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo