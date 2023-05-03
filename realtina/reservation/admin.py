from typing import Any

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect

from reservation.exceptions.models import BaseReservationException
from reservation.models import ReservationModel


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id", "room", "number", "start_date", "end_date", "created", "updated"
    )

    def changeform_view(self, request, *args, **kwargs) -> Any:
        try:
            return super().changeform_view(request, *args, **kwargs)
        except BaseReservationException as exc:
            self.message_user(request, str(exc), level=messages.ERROR)
            return HttpResponseRedirect(request.path)