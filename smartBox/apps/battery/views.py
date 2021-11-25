from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes

from .models import BatteryMessage, BatteryState, CloudAlarm, Box_Battery
from .serializers import BatteryMessageSerializers, BatteryStateSerializers, BatteryCloudAlarmSerializers,Box_BatterySerializers


# # 暂时不用
# class Api_Box_Battery(ListCreateAPIView):
#     queryset = Box_Battery.objects.all()
#     serializer_class = Box_BatterySerializers


class Api_BatteryMsg(ListCreateAPIView):
    queryset = BatteryMessage.objects.all()
    serializer_class = BatteryMessageSerializers


class Api_BatterySta(ListCreateAPIView):
    queryset = BatteryState.objects.all()
    serializer_class = BatteryStateSerializers


class Api_BatteryAlarm(ListCreateAPIView):
    queryset = CloudAlarm.objects.all()
    serializer_class = BatteryCloudAlarmSerializers


@api_view(["POST"])
def box_msg(request):
    data = request._request.body.decode()

    return HttpResponse(data)





