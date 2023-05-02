from django.db import models
from django.utils.translation import gettext_lazy as _


class RoomModel(models.Model):
    name = models.CharField(max_length=1023, unique=True)
    capacity = models.PositiveSmallIntegerField(default=1)
    area = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"({self.name}) suitable for ({self.capacity}) persons."


class ReservationModel(models.Model):
    room = models.ForeignKey(
        RoomModel, related_name="reservations", null=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField()
    end_date = models.DateField()
    number = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.room.name} - From {self.start_date} To {self.end_date}."



