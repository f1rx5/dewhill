from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns=[
    path('master',views.master,name='master'),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
]