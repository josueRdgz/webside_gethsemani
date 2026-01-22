from django.contrib import admin

# Register your models here.
# reflections/admin.py
from .models import Reflection


@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published')
    list_filter = ('is_published', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
