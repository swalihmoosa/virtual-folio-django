from django.contrib import admin

from user.models import Address, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "profession", "gender", "age", "address"]

admin.site.register(Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ["state", "district"]

admin.site.register(Address, AddressAdmin)
