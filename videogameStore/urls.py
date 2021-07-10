from django.urls import path
from .views import ListVideogames, VideogameDetail, VideogameCreate

urlpatterns = [
    path('list/', ListVideogames.as_view(), name="videogameList"),
    path('<int:pk>/', VideogameDetail.as_view(), name="videogameDetail"),
    path('create/', VideogameCreate.as_view(), name="videogameCreate"),
]