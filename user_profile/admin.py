from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name', 'email']

admin.site.register(Profile, ProfileAdmin)
