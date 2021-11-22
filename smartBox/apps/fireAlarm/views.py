from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import FireAlarmMessage, FireAlarmData, Box_FireAlarm
from .serializers import FireAlarmMessageSerializers, FireAlarmDataSerializers, Box_FireAlarmSerializers


class Api_Box_FireAlarm(ListCreateAPIView):
    queryset = Box_FireAlarm.objects.all()
    serializer_class = Box_FireAlarmSerializers


class Api_FireAlarmMsg(ListCreateAPIView):
    queryset = FireAlarmMessage.objects.all()
    serializer_class = FireAlarmMessageSerializers


class Api_FireAlarmData(ListCreateAPIView):
    queryset = FireAlarmData.objects.all()
    serializer_class = FireAlarmDataSerializers














