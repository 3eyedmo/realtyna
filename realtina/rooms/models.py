from django.db import models
from django.utils.translation import gettext_lazy as _
from rooms.exceptions.models import (
    CapacityException, RoomOccupiedException, InvalidDate
)
from datetime import date


class RoomModel(models.Model):
    name = models.CharField(max_length=1023, unique=True)
    capacity = models.PositiveSmallIntegerField(default=1)
    area = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"({self.name}) suitable for ({self.capacity}) persons."

    class Meta:
        unique_together = ("name", "capacity")


class ReservationModel(models.Model):
    room = models.ForeignKey(
        RoomModel, related_name="reservations", null=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField(verbose_name=_("Start of residence date"))
    end_date = models.DateField(verbose_name=_("End of residence date"))
    number = models.PositiveSmallIntegerField(default=1, verbose_name=_("Number of residents"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.room.name} - From {self.start_date} To {self.end_date}."

    def save(self, *args, **kwargs) -> None:
        if self.number > self.room.capacity:
            raise CapacityException("Number is bigger than capacity")
        
        if self.start_date < date.today() or \
                self.end_date <= date.today() or \
                self.end_date <= self.start_date:
            raise InvalidDate("Date format is wrong.")
        date_range = (self.start_date, self.end_date)
        query_if_occupied = self.room.reservations.filter(
            ((models.Q(start_date__in=date_range) | models.Q(end_date__in=date_range)) | \
                  (models.Q(start_date__lte=self.start_date) & models.Q(end_date__gte=self.end_date))) & \
                  (~models.Q(id=self.id))
        ).exists()
        if query_if_occupied:
            raise RoomOccupiedException("Room is ocupied in this period")
        return super().save(*args, **kwargs)
