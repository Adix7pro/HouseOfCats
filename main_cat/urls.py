from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("cat_app.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="main.html"), name="main"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)