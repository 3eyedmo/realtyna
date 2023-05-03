from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import date


class RoomModel(models.Model):
    name = models.CharField(max_length=1023)
    capacity = models.PositiveSmallIntegerField(default=1)
    area = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"({self.name}) suitable for ({self.capacity}) persons."

    class Meta:
        unique_together = ("name", "capacity")


