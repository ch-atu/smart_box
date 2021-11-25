from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse, JsonResponse

from .serializers import AirConditionerSerializers, Box_AirConditionerSerializers
from .models import AirConditionerData, Box_AirConditioner
# Create your views here.


class Api_AirConditioner(ListCreateAPIView):
    serializer_class = AirConditionerSerializers
    queryset = AirConditionerData.objects.all()


class Api_Box_AirConditioner(ListAPIView):
    serializer_class = Box_AirConditionerSerializers
    queryset = Box_AirConditioner.objects.all()











