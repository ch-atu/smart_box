from rest_framework import serializers
from .models import HumitureEquipmentMsg, HumitureSensorData, HumitureThreshold, Box_Humiture


class Box_HumitureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box_Humiture
        fields = '__all__'


class HumitureEMsgSerializers(serializers.ModelSerializer):
    class Meta:
        model = HumitureEquipmentMsg
        fields = '__all__'


class HumitureSensorDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = HumitureSensorData
        fields = '__all__'


class HumitureThresholdSerializers(serializers.ModelSerializer):
    class Meta:
        model = HumitureThreshold
        fields = '__all__'






























