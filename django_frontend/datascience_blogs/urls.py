"""datascience_blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='latest/')),
    url(r'^latest/', include('latest_blogs.urls'))
]
