
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name="homepage_url"),
    url(r'^(?P<post_id>[0-9]+)$', views.post_details, name="post_details_url"),
    url(r'^create/', views.create, name="create_post_url"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
