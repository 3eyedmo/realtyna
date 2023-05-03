from rest_framework import serializers
from rest_framework.exceptions import APIException
from rooms.models import RoomModel
from reservation.models import ReservationModel
from reservation.exceptions.models import BaseReservationException
from reservation.exceptions.serializers import InvalidSaveOperationException



class ReservationSerializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=1023)
    room_capacity = serializers.IntegerField()
    number = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    class Meta:
        fields = ("room_name", "room_capacity", "number", "start_date", "end_date")

    def validate(self, attrs):
        room_name = attrs.get("room_name")
        room_capacity = attrs.get("room_capacity")
        number = attrs.get("number")
        try:
            room = RoomModel.objects.get(name=room_name, capacity=room_capacity)
        except:
            raise serializers.ValidationError({
                "room": f"There is no room with name ({room_name}) and capacity of ({room_capacity})"
            })
        if number > room_capacity:
            raise serializers.ValidationError({
                "room": "The Residents outnumbered the room capacity."
            })
        self.room = room
        
        return super().validate(attrs)

    def save(self, **kwargs):
        reserve = ReservationModel(
            room=self.room,
            number=self.validated_data.get("number"),
            start_date=self.validated_data.get("start_date"),
            end_date=self.validated_data.get("end_date")
        )
        try:
            reserve.save()
        except BaseReservationException as exc:
            raise InvalidSaveOperationException({"datail": str(exc)})
        

