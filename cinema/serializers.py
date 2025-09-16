from rest_framework import serializers

from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("name",
                  "rows",
                  "seats_in_row",
                  "capacity")
