from django.contrib import admin
from web.models import Contact, Login, Signup, Subscribe, Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client", "message"]

admin.site.register(Testimonial, TestimonialAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]

admin.site.register(Contact, ContactAdmin)


admin.site.register(Subscribe)


admin.site.register(Login)


admin.site.register(Signup)
