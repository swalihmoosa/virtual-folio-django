from django.contrib import admin
from web.models import Testimonial

from works.models import 


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client", "message"]

admin.site.register(Testimonial, TestimonialAdmin)