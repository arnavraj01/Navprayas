


from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

#from posts import views as postsViews
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name="signup_url"),
    url(r'^login/', views.loginUser, name="login_url"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
