from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Videogame

class ListVideogames(ListView):
    model = Videogame
    template_name = "listVideogames.html"
    context_object_name = "videogames"


class VideogameDetail(DetailView):
    model = Videogame
    template_name = "videogameDetail.html"
    context_object_name = "videogame"