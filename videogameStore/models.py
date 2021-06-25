from django.db import models

# Create your models here.
GENRES = (
    ("HOR","Horror"),
    ("RPG", "RPG"),
    ("ADV", "Adventure")
    )

class Videogame(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    genre = models.CharField(choices=GENRES, max_length=3)
    price = models.DecimalField(max_digits=20, decimal_places=2)
