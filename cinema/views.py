from rest_framework import viewsets

from .serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer
)

from .models import (
    Actor,
    Genre,
    CinemaHall
)


class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer