from django.contrib import admin
from . models import Device


class DeviceAdmin(admin.ModelAdmin):
	list_display = ['name', 'type', 'state']
	search_fields = ['name']
	list_filter = ['type',]


admin.site.register(Device, DeviceAdmin)
