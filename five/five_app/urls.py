from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from five_app import views
from django.conf import settings
from django.conf.urls.static import static



app_name = "five_app"

urlpatterns = [
url(r'^inscription/',views.register,name= "inscription")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
