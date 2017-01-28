from django.conf.urls import url, include
from rango import views

urlpatterns = [
    url(r'^rango/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about')
]
