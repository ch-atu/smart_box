from django.contrib import admin

# Register your models here.
from .models import AirConditionerData


@admin.register(AirConditionerData)
class AirConditionerAdmin(admin.ModelAdmin):
    pass









