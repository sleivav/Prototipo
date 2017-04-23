from django.conf.urls import url

from app import views

urlpatterns = [
    #/app/
    url(r'^$', views.index, name='index'),
]