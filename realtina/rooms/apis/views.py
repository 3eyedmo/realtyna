from datetime import date


from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import APIException
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rooms.models import RoomModel
from rooms.serializers import RoomSerializer, TargetDateSerializer



dt = openapi.Parameter('dt', openapi.IN_QUERY, description="format: Y-M-D", type=openapi.TYPE_STRING)

class AvailableRoomsApiView(ListAPIView):
    serializer_class = RoomSerializer

    def get_datetime(self):
        target_datetime_raw = self.request.query_params.get("dt")
        try:
            print(target_datetime_raw)
            TargetDateSerializer(instance={"dt": target_datetime_raw})
        except:
            raise APIException({
                "detail": "Invalid date time format"
            }, status_code=400)
        target_datetime_split = target_datetime_raw.split("-")
        target_datetime = date(
                year=int(target_datetime_split[0]),
                month=int(target_datetime_split[1]),
                day=int(target_datetime_split[2])
            )
        if target_datetime < date.today():
            raise APIException({
                "detail": "Invalid date time format"
            })
        return target_datetime

    def get_queryset(self):
        targeted_datetime = self.get_datetime()
        qs = RoomModel.objects.filter(
            ~(Q(reservations__start_date__lte=targeted_datetime)
              & Q(reservations__end_date__gte=targeted_datetime))
        ).distinct()
        return qs
   
    @swagger_auto_schema(manual_parameters=[dt])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

