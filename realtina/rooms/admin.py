from django.contrib import admin
from rooms.models import (
    ReservationModel, RoomModel
)


@admin.register(RoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "capacity", "area", "quantity"
    )

@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id", "room", "start_date", "end_date", "created", "updated"
    )