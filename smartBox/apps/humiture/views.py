from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes


from .models import HumitureEquipmentMsg, HumitureSensorData, HumitureThreshold, Box_Humiture
from .serializers import \
    HumitureSensorDataSerializers, HumitureEMsgSerializers, \
    HumitureThresholdSerializers, Box_HumitureSerializers
# Create your views here.

# # 暂时不用
# class Api_Box_Humiture(ListCreateAPIView):
#     queryset = Box_Humiture.objects.all()
#     serializer_class = Box_HumitureSerializers


class Api_HumitureEMsg(ListCreateAPIView):
    queryset = HumitureEquipmentMsg.objects.all()
    serializer_class = HumitureEMsgSerializers


class Api_HumitureSensorData(ListCreateAPIView):
    queryset = HumitureSensorData.objects.all()
    serializer_class = HumitureSensorDataSerializers


class Api_HumitureThreshold(ListCreateAPIView):
    queryset = HumitureThreshold.objects.all()
    serializer_class = HumitureThresholdSerializers



# 云盒传送过来的数据
@api_view(["POST"])
def box_msg(request):
    data = request._request.body.decode()

    return HttpResponse(data)


