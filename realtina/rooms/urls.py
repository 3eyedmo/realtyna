from django.urls import path
from . import views


app_name="rooms"
urlpatterns = [
    path("booked_list/", views.ListBookedRooms.as_view(), name="get_booked_rooms")
]