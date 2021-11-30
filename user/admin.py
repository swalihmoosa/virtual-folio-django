from django.contrib import admin

from user.models import Address, Client, Education, Experience, Profile, Skill, SkillItems


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "profession", "gender", "age", "address"]

admin.site.register(Profile, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ["state", "district"]

admin.site.register(Address, AddressAdmin)


admin.site.register(Skill)


class SkillItemsAdmin(admin.ModelAdmin):
    list_display = ["skill", "item", "rating"]

admin.site.register(SkillItems, SkillItemsAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ["course", "university", "year", "description"]

admin.site.register(Education, EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["work", "company", "year", "description"]

admin.site.register(Experience, ExperienceAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "description", "image"]

admin.site.register(Client, ClientAdmin)