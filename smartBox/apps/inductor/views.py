from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .models import Box_Inductor
from .serializers import Box_InductorSerializers


# Create your views here.
class API_Box_Inductor(ListCreateAPIView):
    serializer_class = Box_InductorSerializers
    queryset = Box_Inductor.objects.all()












