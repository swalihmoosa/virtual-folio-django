from django.urls import path
from django.urls.conf import include

from web.views import index


app_name = "web"

urlpatterns = [
    path("", index, name="index")
]