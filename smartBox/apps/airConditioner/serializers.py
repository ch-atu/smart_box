from .models import AirConditionerData, Box_AirConditioner
from rest_framework import serializers


class AirConditionerSerializers(serializers.ModelSerializer):
    class Meta:
        model = AirConditionerData
        fields = '__all__'
        # fields = ['preset_humidity', 'discharge_pressure'],


class Box_AirConditionerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box_AirConditioner
        fields = '__all__'










