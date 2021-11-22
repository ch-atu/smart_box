from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .serializers import AirConditionerSerializers, Box_AirConditionerSerializers
from .models import AirConditionerData, Box_AirConditioner
# Create your views here.


class Api_AirConditioner(ListCreateAPIView):
    serializer_class = AirConditionerSerializers
    queryset = AirConditionerData.objects.all()


class Api_Box_AirConditioner(ListCreateAPIView):
    serializer_class = Box_AirConditionerSerializers
    queryset = Box_AirConditioner.objects.all()










