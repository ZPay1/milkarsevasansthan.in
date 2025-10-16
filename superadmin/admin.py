from django.contrib import admin
from .models import *
@admin.register(Admin)
class SuperAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Admin._meta.fields]   