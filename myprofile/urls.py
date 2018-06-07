from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^galeria', views.galeria),
    url(r'^insta', views.insta),
]
