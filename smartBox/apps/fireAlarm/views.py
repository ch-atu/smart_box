from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.generics import ListCreateAPIView
from .models import FireAlarmMessage, FireAlarmData, Box_FireAlarm
from .serializers import FireAlarmMessageSerializers, FireAlarmDataSerializers, Box_FireAlarmSerializers
from rest_framework.decorators import api_view, permission_classes


# # 暂时不用
# class Api_Box_FireAlarm(ListCreateAPIView):
#     queryset = Box_FireAlarm.objects.all()
#     serializer_class = Box_FireAlarmSerializers


class Api_FireAlarmMsg(ListCreateAPIView):
    queryset = FireAlarmMessage.objects.all()
    serializer_class = FireAlarmMessageSerializers


class Api_FireAlarmData(ListCreateAPIView):
    queryset = FireAlarmData.objects.all()
    serializer_class = FireAlarmDataSerializers


@api_view(["POST"])
def box_msg(request):
    data = request._request.body.decode()

    return HttpResponse(data)












