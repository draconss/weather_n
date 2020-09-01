from django.contrib import admin
from .models import *
# Register your models here.
class WAdmin(admin.ModelAdmin):
    list_display = ('city','temp', 'temp_min', 'temp_max', 'pressure', 'humidity','wind_speed','wind_deg','date')
    fieldsets = (
        (None, {
            'fields': ('temp', 'temp_min', 'temp_max', 'pressure', 'humidity','wind_speed','wind_deg')
        }),
    )
admin.site.register(City)
admin.site.register(Weath, WAdmin)