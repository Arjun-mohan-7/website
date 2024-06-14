from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about_us),
    path('signin/', views.sign_in),
    path('signup/', views.sign_up),
    path('contact/', views.contact_us),
]