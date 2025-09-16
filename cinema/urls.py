from django.urls import path, include
from rest_framework import routers

from .views import (
    ActorView,
    GenreView,
    CinemaHallView
)

router = routers.DefaultRouter()

router.register("actors", ActorView)
router.register("genres", GenreView)
router.register("cinema_halls", CinemaHallView)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"

