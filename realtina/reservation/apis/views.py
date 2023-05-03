from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from reservation.serializers import ReservationSerializer



class CreateReservationView(
    CreateModelMixin,
    GenericAPIView
):
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
