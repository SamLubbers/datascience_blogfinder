"""latest_blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
