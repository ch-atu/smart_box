from rest_framework import serializers
from .models import Box_Inductor


class Box_InductorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box_Inductor
        fields = '__all__'
















