from typing import Any
from datetime import date

from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.db.models import Q
from rooms.models import RoomModel
from reservation.models import ReservationModel

class ListBookedRooms(ListView):
    template_name="rooms/index.html"
    paginate_by=5
    def get_queryset(self) -> QuerySet[Any]:
        qs = RoomModel.objects.filter(Q(reservations__end_date__gte=date.today())).distinct()
        return qs