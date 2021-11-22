from django.contrib import admin

# Register your models here.
from .models import BatteryMessage, BatteryState, CloudAlarm


@admin.register(BatteryMessage, BatteryState, CloudAlarm)
class BatteryAdmin(admin.ModelAdmin):
    pass



