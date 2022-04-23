from django.urls import path
from .views import send_user


app_name = 'account'

urlpatterns = [
    path('send_email', send_user, name='send_user'),
]