from django.contrib import admin
from django.http.request import HttpRequest
from rooms.models import RoomModel




@admin.register(RoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "capacity", "area"
    )


