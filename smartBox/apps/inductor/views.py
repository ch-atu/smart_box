from django.shortcuts import render
from django.http.response import HttpResponse


from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes


from .models import Box_Inductor
from .serializers import Box_InductorSerializers


# Create your views here.
# # 暂时不用
# class API_Box_Inductor(ListCreateAPIView):
#     serializer_class = Box_InductorSerializers
#     queryset = Box_Inductor.objects.all()


@api_view(["POST"])
def box_msg(request):
    data = request._request.body.decode()

    return HttpResponse(data)










