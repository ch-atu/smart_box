from django.contrib import admin

# Register your models here.
from .models import FireAlarmMessage, FireAlarmData


@admin.register(FireAlarmMessage, FireAlarmData)
class FireAlarmAdmin(admin.ModelAdmin):
    pass











