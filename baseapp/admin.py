from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(World)
class AdminWorld(admin.ModelAdmin):
    list_display = ('world_name', 'world_description', 'get_image')

    @staticmethod
    def get_image(obj):
        try:
            return format_html('<img src="{}" width="300" height="200"/>'.format(obj.world_image.url))
        except ValueError:
            pass


@admin.register(System)
class AdminSystem(admin.ModelAdmin):
    list_display = ('system_name', 'system_description', 'system_slug')
    prepopulated_fields = {'system_slug': ('system_name', )}
