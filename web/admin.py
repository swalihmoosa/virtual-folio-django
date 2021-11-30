from django.contrib import admin
from web.models import Contact, Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client", "message"]

admin.site.register(Testimonial, TestimonialAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]

admin.site.register(Contact, ContactAdmin)