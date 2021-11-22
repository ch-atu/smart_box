from django.contrib import admin

# Register your models here.
from .models import InductorMsg


@admin.register(InductorMsg)
class InductorAdmin(admin.ModelAdmin):
    pass
