from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('User_email/', views.Sendemail),
    path('User_resetpassword/<str:id>', views.password_change),
]

