from django.contrib import admin
from .models import *
import datetime
import ipaddress
import random
from .apis_request import req
from django.urls import reverse
from django.utils.html import format_html


class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'id','email', 'membership','formatted_create_at')
    def formatted_create_at(self, obj):
        timestamp_seconds = obj.create_at / 1000
        formatted_date = datetime.datetime.fromtimestamp(timestamp_seconds).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date
    formatted_create_at.short_description = 'Create At'

    

admin.site.register(User,UserAdmin)