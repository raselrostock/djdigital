from django.urls import path
from .views import UserRegistrationView, ProfileView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('/profile/', ProfileView, name='profile'),
]
