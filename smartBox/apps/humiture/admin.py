from django.contrib import admin

# Register your models here.
from .models import HumitureEquipmentMsg, HumitureSensorData, HumitureThreshold


@admin.register(HumitureEquipmentMsg, HumitureSensorData, HumitureThreshold)
class HumitureAdmin(admin.ModelAdmin):
    pass
