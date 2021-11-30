from django.contrib import admin

from works.models import Category, Project, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

admin.site.register(Service, ServiceAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "is_completed", "clients"]

admin.site.register(Project, ProjectAdmin)


admin.site.register(Category)