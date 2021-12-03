from django.urls import path

from web.views import contact, index, subscribe, login, signup, signup_page
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("contact",contact,name="contact"),
    path("subscribe",subscribe,name="subscribe"),
    path("login",login,name="login"),
    path("signup_page",signup_page,name="signup_page"),
    path("signup",signup,name="signup")

]