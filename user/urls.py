from django.urls import path

from web.views import index


app_name = "user"

urlpatterns = [
    path("", index, name="index")
]