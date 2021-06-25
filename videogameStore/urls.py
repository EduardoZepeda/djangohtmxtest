from django.urls import path
from .views import ListVideogames, VideogameDetail

urlpatterns = [
    path('list/', ListVideogames.as_view(), name="videogameList"),
    path('<int:pk>/', VideogameDetail.as_view(), name="videogameDetail"),
]