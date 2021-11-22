from rest_framework import serializers
from .models import FireAlarmMessage, FireAlarmData, Box_FireAlarm


class Box_FireAlarmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box_FireAlarm
        fields = '__all__'


class FireAlarmMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = FireAlarmMessage
        fields = '__all__'


class FireAlarmDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = FireAlarmData
        fields = '__all__'





























