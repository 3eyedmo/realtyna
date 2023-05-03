from django.urls import path
from . import views


app_name = "reservation"
urlpatterns = [
    path("", views.CreateReservationView.as_view(), name="create_reservation")
]