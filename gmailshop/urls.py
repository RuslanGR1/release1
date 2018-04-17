from django.contrib import admin
from django.conf.urls import url
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'gmail&(\w{25})$', views.final_page, name='final'),
    url(r'gmail&type=(?P<type>[0-9a-z]+)/', views.first_form, name='form'),
    url(r'gmail&([0-9a-z]{2})/(\w+)', views.txt_download),
]