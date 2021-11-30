from django.contrib import admin

from works.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

admin.site.register(Service, ServiceAdmin)