from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^register$', views.register),
        url(r'^display$', views.display),
        url(r'^addquote$', views.display),
]