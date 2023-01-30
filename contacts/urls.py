from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('test/', views.test, name='test')
]
