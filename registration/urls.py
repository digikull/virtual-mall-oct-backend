from django.urls import path,include
from .views import Registration #importing Register View
urlpatterns = [

    path('register/',  Registration.as_view())# For Registre the user
]
