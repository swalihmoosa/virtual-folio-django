from django.urls import path

from user.views import index


app_name = "user"

urlpatterns = [
    path("", index, name="index")
]