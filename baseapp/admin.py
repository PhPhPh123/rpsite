from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(World)
class AdminWorld(admin.ModelAdmin):
    list_display = ('world_name', 'world_description', 'get_image')

    @staticmethod
    def get_image(obj):
        try:
            return format_html('<img src="{}" width="200" height="200"/>'.format(obj.world_image.url))
        except ValueError:
            pass
    get_image.short_description = 'Картинка'

