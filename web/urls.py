from django.urls import path

from web.views import contact, index, subscribe
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("contact",contact,name="contact"),
    path("subscribe",subscribe,name="subscribe")
]