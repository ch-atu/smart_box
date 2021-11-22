from rest_framework import serializers
from .models import BatteryMessage, BatteryState, CloudAlarm, Box_Battery


class Box_BatterySerializers(serializers.ModelSerializer):
    class Meta:
        model = Box_Battery
        fields = '__all__'


class BatteryMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = BatteryMessage
        fields = '__all__'


class BatteryStateSerializers(serializers.ModelSerializer):
    class Meta:
        model = BatteryState
        fields = '__all__'


class BatteryCloudAlarmSerializers(serializers.ModelSerializer):
    class Meta:
        model = CloudAlarm
        fields = '__all__'





