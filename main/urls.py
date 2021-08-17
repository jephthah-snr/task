from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home-view'),
    path('success/', views.Contact_form, name='contact-view')
]
