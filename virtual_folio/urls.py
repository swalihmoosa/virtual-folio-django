from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("",include("web.urls",namespace="web")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
