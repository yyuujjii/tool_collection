from django.urls import path
from testapp import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contents/', views.contents, name='contents'),
    path('contact/', views.contact, name='contact'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('comp/', views.comp, name='comp'),
]
