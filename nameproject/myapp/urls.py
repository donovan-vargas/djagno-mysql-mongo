# coding=utf-8
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^get_grades/$', views.get_grades, name='myapp.get_grades')
]
