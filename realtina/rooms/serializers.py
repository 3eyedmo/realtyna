from rest_framework import serializers

from rooms.models import RoomModel

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomModel
        fields=("id", "name", "capacity", "area")


class TargetDateSerializer(serializers.Serializer):
    dt = serializers.DateField()