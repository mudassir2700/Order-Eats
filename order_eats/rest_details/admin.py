from django.contrib import admin

# Register your models here.
from .models import restaurant_details,setting

admin.site.register(restaurant_details)
admin.site.register(setting)