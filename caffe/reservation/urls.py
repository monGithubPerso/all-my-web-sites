from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path(r'', views.reservation, name="reservation"),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
