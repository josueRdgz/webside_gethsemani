from django.contrib import admin

# Register your models here.
# core/admin.py
from django.contrib import admin
from .models import Elder


@admin.register(Elder)
class ElderAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
