from django.urls import path
from . import views

app_name="rooms_api"
urlpatterns = [
    path("awailable/", views.AvailableRoomsApiView.as_view(), name="awailable_rooms")
]
